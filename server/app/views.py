from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Vercel! Django is running 🚀</h1>")
