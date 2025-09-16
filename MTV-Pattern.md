## MTV Pattern (Model–Template–View)
    Django doesn’t use the classic MVC naming. Instead, it uses MTV:

    Model → Handles database (tables, queries, relationships)

    Template → Handles frontend (HTML, CSS, JS, dynamic rendering)

    View → Handles logic (receives request, fetches data from model, sends to template, returns response)

## User Request → URL Dispatcher → View → Model (optional) → Template → Response

## Example Project: Simple Blog (Posts)

    We’ll build a tiny blog app where:

    Model = BlogPost

    Template = HTML page showing posts

    View = Logic to fetch posts and render them

Step 1 - Create App - python manage.py startapp blog
Step 2 - add 'blog' to INSTALLED_APPS in mysite/settings.py 
step 3 - create models blog/models.py
    run migration 
    python manage.py makemigrations
    python manage.py migrate



