# ✍️ AI Blog Article Generator 🤖

Generate high-quality blog articles instantly using **Google Gemini AI** through a clean and responsive web interface built with **Django**.

---

## 📌 Overview

AI Blog Article Generator is a web application that allows users to generate blog articles on any topic using Google's Gemini AI model. Users can create an account, log in, generate AI-powered content, and browse previously generated articles.

The project demonstrates the integration of modern AI APIs with Django while implementing user authentication, dynamic templates, and database management.

---

> [!IMPORTANT]
> **Please update all dependencies before running this project.**
>
> AI SDKs and YouTube-related libraries receive frequent updates, and older versions may cause compatibility issues or runtime errors.
>
> Before starting the project, run:
>
> ```bash
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt
> python -m pip install --upgrade google-genai yt-dlp
> ```
>
> **Google Gemini models are updated regularly.** If you encounter errors such as:
>
> - Model not found
> - Deprecated model
> - Invalid API request
>
> check the latest supported models in the official Gemini documentation and update the model name in the source code accordingly.
>
> **Official Documentation**
>
> - https://ai.google.dev/gemini-api/docs
> - https://ai.google.dev/gemini-api/docs/models

---

# ✨ Features

- 🔐 User Authentication (Signup & Login)
- 🤖 Generate AI-powered blog articles
- 📝 Browse previously generated blogs
- 🎨 Responsive and clean user interface
- 📚 Store generated blogs in SQLite database
- ⚡ Fast content generation using Google Gemini API
- 📱 Mobile-friendly pages
- 📬 Contact page

---

# 📸 Demo

## 🏠 Home Page

<img width="1909" height="932" alt="Home Page" src="https://github.com/user-attachments/assets/0675c14f-75b0-4253-abe3-8f09a91bf80d" />

---

## 🔑 Login Page

<img width="1916" height="936" alt="Login Page" src="https://github.com/user-attachments/assets/6346c06b-d7a9-4d99-9639-6002db1e0aa6" />

---

## ✍️ Generate Blog

<img width="1907" height="931" alt="Generate Blog" src="https://github.com/user-attachments/assets/104cb241-a8c9-43ad-817b-74169e6b30a1" />

---

## 📖 Generated Blog

<img width="1817" height="932" alt="Generated Blog" src="https://github.com/user-attachments/assets/b01d8e0f-3f5a-4c92-aa4b-010279d2bae5" />

---

## 📚 All Blogs

<img width="1911" height="936" alt="All Blogs" src="https://github.com/user-attachments/assets/e1f66ffb-25c9-48b5-8818-a731dec5946d" />

---

# 🛠 Tech Stack

- **Python**
- **Django**
- **Google Gemini API**
- **SQLite**
- **HTML**
- **CSS**
- **JavaScript**
- **Bootstrap**
- **yt-dlp**
- **Markdown**

---

# 📂 Project Structure

```text
AI_Blog_Article_Generator/

│
├── ai_blog_app/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blog_generator/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── manage.py
├── requirements.txt
├── .gitignore
├── db.sqlite3
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/rohit-singh-3200/ai_blog_article_generator.git
```

---

## 2. Navigate to the project

```bash
cd ai_blog_article_generator
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it

```bash
source venv/bin/activate
```

---

## 4. Install & Update Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install --upgrade google-genai yt-dlp
```

---

## 5. Create a `.env` File

Create a `.env` file in the project root and add your Gemini API key:

```env
API_KEY=your_google_gemini_api_key
```

You can generate an API key from:

https://aistudio.google.com/apikey

---

## 6. Run Database Migrations

```bash
python manage.py migrate
```

---

## 7. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# 🚀 How It Works

```text
User

↓

Login / Signup

↓

Paste YouTube Video URL

↓

yt-dlp extracts audio

↓

Gemini API transcribes audio

↓

Gemini generates a blog article

↓

Blog is saved to the database

↓

User can view all previously generated blogs
```

---

# 📚 Future Improvements

- 🖼 AI Image Generation
- 📄 Export blogs as PDF
- 📑 Export blogs as Word documents
- 🌐 Multi-language support
- 🎭 Blog writing style selection
- 🎯 SEO optimization
- 🔖 Save favorite blogs
- 📊 User analytics dashboard
- ☁️ AWS Deployment
- 🐳 Docker Support
- 🔍 AI-generated blog summaries

---

# 👨‍💻 Author

**Rohit Kumar Singh**

- **GitHub:** https://github.com/rohit-singh-3200
- **LinkedIn:** https://www.linkedin.com/in/rohitkpsingh

---

⭐ If you found this project useful, consider giving it a **Star ⭐** to support the project!
