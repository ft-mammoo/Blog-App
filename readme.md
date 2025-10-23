# Django Blog Application

A feature-rich blogging platform built with Django, allowing users to create, edit, and interact with blog posts.

## Features

- 👤 User Authentication (Login/Signup)
- ✍️ Create, Edit, and Delete Blog Posts
- 🏷️ Category Management
- 👍 Like/Dislike System
- 📝 Rich Text Editor
- 💼 User-friendly Forms
- 🎨 Bootstrap-based Responsive Design

## Technology Stack

- Django 4.2+
- Python 3.10+
- Bootstrap 4
- SQLite Database
- CKEditor for Rich Text Editing

## Installation

1. Clone the repository
```bash
git clone https://github.com/ft-mammoo/Blog-App.git
cd Blog-App
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply database migrations
```bash
python manage.py migrate
```

5. Create a superuser (Admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the blog.

## Project Structure

```
blog/               # Main project directory
├── blog/           # Project settings
├── members/        # User authentication app
│   └── templates/  # Login/Signup templates
└── theblog/        # Blog functionality app
    └── templates/  # Blog templates
```

## Features Details

### User Authentication
- User registration with signup form
- Login/logout functionality
- User profile management

### Blog Posts
- Create new blog posts with rich text editor
- Edit existing posts
- Delete posts
- Add post snippets for preview
- Categorize posts
- Like/Dislike system

### Categories
- Create and manage post categories
- Filter posts by category
- Category-based navigation

## Contributing

We love your input! We want to make contributing to Blog-App as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

Check out our [Contributing Guide](CONTRIBUTING.md) for detailed information on how to contribute to this project.

## Acknowledgments

- Special thanks to [Codemy.com](https://codemy.com/) for their excellent Django tutorial that served as the foundation for this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
