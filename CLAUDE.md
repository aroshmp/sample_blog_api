# Claude Code Instructions for Sample Blog API

## Project Overview
This is a Django REST Framework blog API with the following features:
- User profiles with bio and social links
- Blog posts with rich text content
- Categories for organizing posts
- Comments system
- Like functionality for posts
- PostgreSQL database backend

## Project Structure
- `blog/` - Main blog application containing models, serializers, viewsets, and URLs
- `sample_blog_api/` - Project settings and configuration
- `manage.py` - Django management script

## Technology Stack
- Django 5.2.7
- Django REST Framework 3.16.1
- PostgreSQL (via psycopg2-binary)
- CKEditor for rich text editing
- Python-dotenv for environment variables

## Key Models
- **Profile**: User profile with bio, profile picture, and social links
- **Category**: Blog post categories
- **Post**: Blog posts with title, body, author, category, and likes
- **Comment**: Comments on posts

## Development Guidelines

### Environment Setup
1. Ensure PostgreSQL is running and accessible
2. Required environment variables in `.env`:
   - PGHOST
   - PGDATABASE
   - PGPORT
   - PGUSER
   - PGPASSWORD

### Running the Project
```bash
# Run migrations
python manage.py migrate

# Create superuser (if needed)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Code Style
- Follow Django and PEP 8 conventions
- Use meaningful variable and function names
- Keep models, serializers, and viewsets organized in their respective files

### API Development
- Use Django REST Framework viewsets for CRUD operations
- Define serializers in `blog/serializers.py`
- Define viewsets in `blog/viewsets.py`
- Register URL patterns in `blog/urls.py`

### Database Changes
- Always create and run migrations after model changes:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### Testing
- Write tests in `blog/tests.py`
- Run tests with: `python manage.py test`

### Security Notes
- SECRET_KEY is currently exposed in settings.py - should be moved to environment variables
- DEBUG is True - should be False in production
- ALLOWED_HOSTS is set to ['*'] - should be restricted in production

## Common Tasks

### Adding a New Model
1. Define model in `blog/models.py`
2. Create serializer in `blog/serializers.py`
3. Create viewset in `blog/viewsets.py`
4. Register URL in `blog/urls.py`
5. Run `python manage.py makemigrations` and `python manage.py migrate`

### Adding a New API Endpoint
1. Create/update serializer if needed
2. Create/update viewset with appropriate actions
3. Register route in `blog/urls.py` using router

### Adding New Dependencies
1. Add to `requirements.txt`
2. Install with: `pip install -r requirements.txt`
3. Update `INSTALLED_APPS` in settings if it's a Django app

## Important Files
- `sample_blog_api/settings.py` - Project configuration
- `sample_blog_api/urls.py` - Root URL configuration
- `blog/models.py` - Database models
- `blog/serializers.py` - API serializers
- `blog/viewsets.py` - API viewsets/views
- `blog/urls.py` - Blog app URL patterns

## Notes
- The project uses RichTextField from CKEditor for rich text content
- User authentication is built-in via Django's auth system
- The API follows REST principles via Django REST Framework
- Media files (images) are handled for profile pictures and post headers