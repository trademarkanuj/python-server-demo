from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>✅ Django Stateless Bot Running!</h1><p>Everything looks good.</p>")

def api_test(request):
    return JsonResponse({"message":"Hello from Django API ✅"})
