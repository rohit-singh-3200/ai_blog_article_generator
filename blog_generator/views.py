import yt_dlp
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from google import genai
from .models import Blogpost
import markdown


def index(request):
    return render(request, 'index.html')

def my_view(request):
    return render(request, 'index.html', {'MEDIA_URL': settings.MEDIA_URL})

def contact_us(request):
    return render(request,'contact.html')


def yt_title(link):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        return info.get("title", "Unknown Title")


def download_Audio(link):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link, download=False)  # Get video info without downloading
            filename = f"{info['title']}.mp3"
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Check if file already exists
    if os.path.exists(file_path):
        return file_path  # Use existing file

        # Set up download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(settings.MEDIA_ROOT, "%(title)s.%(ext)s"),
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
       }],
            'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',
            'quiet': True
        }

        # Download the audio if it doesn't exist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    return file_path

def get_transcription(link):

    client = genai.Client(api_key="AIzaSyBhJ6QwfWk3dWjo6gbjdMXoB89KybH2Rtk")
    audio_file=download_Audio(link)
    myfile = client.files.upload(file=audio_file)

    response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=['This is a youtube video, transcribe this video, properly format it , in short 2-3 paragraphs',myfile]
)

    return response.text

def generate_blog_from_transcription(transcription):
    """ Uses Google Gemini to generate a blog from the transcript. """
    try:
        client = genai.Client(api_key="AIzaSyBhJ6QwfWk3dWjo6gbjdMXoB89KybH2Rtk")
        prompt = f"Based on the following transcript, write an engaging blog without any text formatting, have a heading:\n\n {transcription} \n\n"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

        Blog_markdown= response.text if hasattr(response, 'text') else None
        blog_html=markdown.markdown(Blog_markdown)
        return blog_html

    except Exception as e:
        print(f"Error generating blog content: {e}")
        return None

@csrf_exempt
def generate_blog(request):
    """ Handles YouTube link submission, extracts transcript, and generates a blog post. """
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)
        yt_link = data.get('link')
        if not yt_link:
            return JsonResponse({'error': 'No YouTube link provided'}, status=400)

        transcription = get_transcription(yt_link)
        if not transcription:
            return JsonResponse({'error': 'Failed to generate transcript'}, status=500)
        
        title=yt_title(yt_link)

        blog_content = generate_blog_from_transcription(transcription)
        if not blog_content:
            return JsonResponse({'error': 'Failed to generate blog article'}, status=500)
        
        if not request.user.is_authenticated:
            return JsonResponse({"error": "You must be logged in to generate a blog."}, status=403)
        
        new_blog_post=Blogpost.objects.create(
            user=request.user,
            youtube_title=title,
            youtube_link=yt_link,
            generated_content=blog_content,
        )
        new_blog_post.save()

        return JsonResponse({'content': blog_content})
    

    except Exception as e:
        import traceback
        print(f"Unexpected error: {e}")
        traceback.print_exc()  # This prints the full error details
        return JsonResponse({'error': str(e)}, status=500)


def blog_list(request):
    blog_posts=Blogpost.objects.filter(user=request.user)
    return render(request,'blogs.html',{'blog_posts':blog_posts})

def blog_detail(request, pk):
    blog_detail=Blogpost.objects.get(id=pk)
    if request.user==blog_detail.user:
       return render (request, 'blog_page.html',{'blog_detail':blog_detail})
    else:
        return redirect('/')
    

def user_login(request):
    """ Handles user login. """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': "Invalid username or password"})

    return render(request, 'login.html')


def user_signup(request):
    """ Handles user signup. """
    if request.method == "POST":
        username = request.POST.get('username')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('passwordagain')

        if password != repeat_password:
            return render(request, 'signup.html', {'error_message': "Passwords do not match!"})

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')
        except:
            return render(request, 'signup.html', {'error_message': "Error creating account"})

    return render(request, 'signup.html')


def user_logout(request):
    """ Logs out the user. """
    logout(request)
    return redirect('/')
