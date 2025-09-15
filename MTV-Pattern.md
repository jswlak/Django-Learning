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

Create App - python manage.py startapp blog
