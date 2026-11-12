# Prompt-Vault 🚀
### A Community-Driven Prompt Management, Discovery & Analytics Platform

AI Prompt Library is a web-based platform designed to help users create, organize, discover, bookmark, and share high-quality AI prompts in one centralized space.

With the growing adoption of Large Language Models (LLMs) such as ChatGPT, Claude, Gemini, and Copilot, effective prompt engineering has become an important skill. However, useful prompts are often scattered across different platforms, making them difficult to organize, retrieve, and evaluate.

AI Prompt Library addresses this problem by providing a structured, community-driven repository for managing and discovering reusable AI prompts.

---

## ✨ Key Features

The following features define the planned application scope.

### 👤 User Management
- User registration and authentication.
- Secure login and logout.
- User profile creation and management.
- Personalized user dashboard.

### 📝 Prompt Management
- Create, edit, update, and delete prompts.
- Add titles, descriptions, and detailed prompt content.
- Assign categories and tags.
- View individual prompt details.
- Copy prompts directly to the clipboard.

### 📚 Collections & Bookmarks
- Create personalized prompt collections.
- Save and organize favorite prompts.
- Add or remove prompts from collections.
- Maintain a personal prompt library.

### 🔍 Search & Discovery
- AJAX-powered dynamic search.
- Search prompts by title, description, and content.
- Filter prompts by categories and tags.
- Sort by popularity, ratings, and recency.
- Discover trending and recently published prompts.

### ⭐ Community Engagement
- Rate and review prompts.
- View average prompt ratings.
- Bookmark useful prompts.
- Explore prompts shared by other users.

### 📊 Analytics & Reporting
- Track prompt popularity and engagement.
- Generate user activity reports.
- Analyze prompt ratings and usage statistics.
- Export reports in CSV and PDF formats.

### 🛡️ Administration
- Manage users and published prompts.
- Manage categories and tags.
- Moderate reported content.
- Monitor platform activity through Django Admin.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Client-side scripting | JavaScript |
| Asynchronous interactions | AJAX, Fetch API |
| Backend | Python, Django |
| Database (Development) | SQLite |
| Database (Production) | PostgreSQL |
| Data visualization | Chart.js |
| PDF generation | ReportLab |
| CSV generation | Python CSV / Pandas |
| Version control | Git, GitHub |
| Development environment | Visual Studio Code |
| Deployment | Render / Railway |

---

## 🏗️ Project Architecture

The application follows a modular Django architecture, separating frontend presentation, application logic, and database operations.

```text
Prompt-Vault/
│
├── config/                  # Django project configuration
│
├── apps/
│   ├── accounts/            # Authentication and profiles
│   ├── prompts/             # Prompt CRUD operations
│   ├── taxonomy/            # Categories and tags
│   ├── collections/         # Personal prompt collections
│   ├── interactions/        # Bookmarks, ratings and reviews
│   ├── search/              # AJAX search and filtering
│   └── reports/             # Analytics and report generation
│
├── templates/               # Shared HTML templates
│
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript and AJAX
│   └── images/              # Static images and assets
│
├── media/                   # User-uploaded media
│
├── tests/                   # Integration and system tests
│
├── deployment/              # Deployment configurations
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

Each Django application is responsible for a specific functional module, promoting maintainability, separation of concerns, and easier future expansion.

---

## 🗄️ Database Design

The application uses a relational database structure managed through Django ORM.

| Entity | Description |
|---|---|
| User | Stores user accounts and profile information |
| Prompt | Stores prompt content, descriptions, authors, and timestamps |
| Category | Organizes prompts into predefined categories |
| Tag | Enables flexible prompt classification |
| Collection | Stores personalized user-created collections |
| CollectionItem | Establishes relationships between collections and prompts |
| Bookmark | Stores user-saved prompts |
| Rating | Stores prompt ratings and user feedback |

### Core Relationships

- A user can create multiple prompts.
- A category can contain multiple prompts.
- A prompt can have multiple tags.
- A user can create multiple collections.
- A collection can contain multiple prompts.
- A user can bookmark multiple prompts.
- A user can rate a particular prompt once, with the ability to update the rating.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/er-ishita/Prompt-Vault.git

cd Prompt-Vault
```

### 2. Create a Virtual Environment

**Windows (PowerShell):**

```powershell
py -3.12 -m venv venv

.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Do not commit your `.env` file or expose sensitive credentials.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Django Admin will be available at:

```text
http://127.0.0.1:8000/admin/
```

---

## 🔄 Application Workflow

1. **Registration:** Users create accounts and authenticate.
2. **Prompt Creation:** Authenticated users publish prompts with descriptions, categories, and tags.
3. **Discovery:** Users search, filter, and browse available prompts.
4. **Engagement:** Users bookmark, rate, and review prompts.
5. **Organization:** Users create collections to organize saved prompts.
6. **Analytics:** The platform tracks engagement and generates reports.
7. **Administration:** Administrators manage users, content, and platform activity.

---

## 🔮 Future Enhancements

Potential extensions to the platform include:

- **AI-Based Recommendations:** Recommend prompts based on user interests and browsing activity.
- **Prompt Version Control:** Track prompt modifications and restore previous versions.
- **Prompt Variables:** Support reusable templates with customizable placeholders.
- **LLM Integration:** Test prompts against supported AI models.
- **Prompt Performance Analytics:** Compare prompt effectiveness using structured evaluation metrics.
- **Community Features:** Introduce user following, discussions, and collaborative collections.
- **REST API:** Enable integration with external applications and mobile clients.

---

## 🎯 Project Objective

AI Prompt Library aims to create an organized and accessible ecosystem for prompt engineering enthusiasts, developers, students, and AI practitioners.

By combining Django-based full-stack development, database management, asynchronous interactions, community engagement, and analytics, the platform demonstrates practical implementation of modern web application development concepts.

---
