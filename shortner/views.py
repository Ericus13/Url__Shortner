from django.http import request, HttpResponse
from django.shortcuts import redirect, render
from uuid import uuid4
from .models import Url
# Create your views here.

def index(request):
    return render(request, "interface.html")

def create(request):
    if request.method == 'POST':
        l = request.POST["link"]
        uid = str(uuid4())[:5]
        new_url = Url(uuid =uid)
        new_url.save
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://' + url_details.link)
