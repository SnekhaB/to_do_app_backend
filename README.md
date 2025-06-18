
# To do App
# 📝 To-Do App Backend

This is the backend API for the To-Do application built with **Flask**. It provides endpoints for managing tasks (GET, POST, DELETE, etc.) and supports CORS to communicate with the frontend.

---

## 🚀 Tech Stack

- Python 3.9+
- Flask
- Flask-CORS
- Gunicorn (for production)
- Render (for deployment)

---

## 📂 Project Structure

to_do_app_backend\

├── app.py\
├── requirements.txt\
├── Procfile\
└── README.md

## Deployment

To deploy this project run

Set Build Command: 
```bash
pip install -r requirements.txt
```
In requirements.txt make sure it includes:

flask\
flask-cors\
gunicorn

Set Start Command: 
```bash
gunicorn app:app
```
