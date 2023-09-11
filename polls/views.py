from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world. you're are the polls index.")