from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World! 🚀")

def about(request):
    return HttpResponse("This is the About Page")
