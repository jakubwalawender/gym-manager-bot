from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    output = "HAHA"
    return HttpResponse(output)