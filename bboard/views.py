from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Здесь будет сайт</h1>")

# Create your views here.
