from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>✅ Django & Bot Running! demo</h1><p>Everything looks good.</p>")

def api_test(request):
    return JsonResponse({"message":"Hello from Django API ✅"})
