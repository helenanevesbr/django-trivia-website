# Django Trivia Website

## Introduction
A Trivia website for users to test their knowledge on Django framework. Built with Python 3.11 and Django 4.2 with the purpose of practicing.  
[Original project](https://github.com/ariannedee/intro-to-django)  
[OReilly Course](https://learning.oreilly.com/course/introduction-to-django/9780138320775/)

### Live Site
Check out the live version of the trivia website here: [Trivia Website](https://trivia-ariannedee.pythonanywhere.com/)

## Technologies
- **Backend Framework**: Django 5.0.2
- **Programming Language**: Python 3.10.12
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript (Django Templates)

## Local Setup
To set up the project locally, follow these steps:

1. **Clone the repository**
```bash
git clone <repository-url>
cd trivia-website
```
  
2. **Create and activate a virtual environment**
For Unix/macOS:
```bash
python3 -m venv env
source venv/bin/activate
```
For Windows:
```bash
py -m venv env
.\env\Scripts\activate
```
  
3. **Install the dependencies**
```bash
pip install -r requirements.txt
```
  
4. **Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
```
  
5. **Run the development server**
```bash
python manage.py runserver
```
  
Access the website at `http://127.0.0.1:8000/`

## Features
- Basic user login/singup
- Staff can edit questions using Django forms
- Admin site for managing users and questions
- Sessions for remembering quiz state
- Production and local settings
- Environs and .env file
- Uploaded user avatars
- Django Debug Toolbar configured in development
