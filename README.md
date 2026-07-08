# ✍️ AI Blog Article Generator 🤖

Generate high-quality blog articles instantly using **Google Gemini AI** through a clean and responsive web interface built with **Django**.

---

## 📌 Overview

AI Blog Article Generator is a web application that allows users to generate blog articles on any topic using Google's Gemini AI model. Users can create an account, log in, generate AI-powered content, and browse previously generated articles.

The project demonstrates the integration of modern AI APIs with Django while implementing user authentication, dynamic templates, and database management.

---

## ✨ Features

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

## Home Page

(Add Screenshot Here)

---

## Login Page

(Add Screenshot Here)

---

## Generate Blog

(Add Screenshot Here)

---

## Generated Blog

(Add Screenshot Here)

---

## All Blogs

(Add Screenshot Here)

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

---

# 📂 Project Structure

```
AI_Blog_Article_Generator/

│
├── ai_blog_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── blog_generator/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/rohit-singh-3200/ai_blog_article_generator.git
```

## 2. Navigate to the project

```bash
cd ai_blog_article_generator
```

## 3. Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 6. Run migrations

```bash
python manage.py migrate
```

---

## 7. Start the development server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 🚀 How It Works

```
User

↓

Login / Signup

↓

Enter Blog Topic

↓

Django Backend

↓

Gemini API

↓

AI Generates Blog

↓

Store in Database

↓

Display to User
```

---

# 📚 Future Improvements

- 🖼 AI Image Generation
- 📄 Export blogs as PDF
- 📑 Export as Word Document
- 🌐 Multi-language support
- 🧠 Blog tone selection
- 🎯 SEO optimization
- 🔖 Save favorite blogs
- 📊 Blog analytics dashboard
- ☁️ AWS Deployment
- 🐳 Docker Support

---

# 👨‍💻 Author

**Rohit Kumar Singh**

- GitHub: https://github.com/rohit-singh-3200
- LinkedIn: https://www.linkedin.com/in/rohitkpsingh

---

⭐ If you found this project useful, consider giving it a star!
