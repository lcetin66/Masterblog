# Masterblog 🚀

Masterblog is a modern, minimalist blog application built with Flask. It allows users to create, read, update, and delete (CRUD) blog posts stored in a JSON-based local database.

[![Built with Flask](https://img.shields.io/badge/Flask-v3.0+-blue?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 📁 Project Structure

```bash
.
├── app.py              # Main Flask application logic
├── data/
│   └── my_blog_posts.json   # Local JSON database for blog storage
├── static/
│   └── style.css       # Custom minimalist CSS styling
└── templates/
    ├── add.html        # New blog post creation page
    ├── index.html      # Blog feed and home page
    └── update.html     # Blog post editing page
```

## ✨ Features

- **CRUD Functionality**: Create, Read, Update, and Delete blog posts.
- **Persistent Storage**: All posts are saved in a structured JSON file.
- **Minimalist UI**: Clean, responsive, and easy-to-use interface.
- **Dynamic ID Generation**: Automatic unique ID assignment for new posts.
- **Documentation**: Well-commented codebase for easy understanding.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3 (Minimalist Custom Design)
- **Database**: JSON (File-based)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your machine.
- Flask library.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lcetin66/Masterblog.git
   cd Masterblog
   ```

2. **Install dependencies**:
   ```bash
   pip install Flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the blog**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📝 Usage

1. **View Posts**: The homepage lists all current blog stories.
2. **Add Post**: Click "+ Create New Post" on the home screen.
3. **Edit Post**: Click the "Edit" button on any post card to modify it.
4. **Delete Post**: Click the "Delete" button to remove a post from the database.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
