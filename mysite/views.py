from django.shortcuts import render
from mysite.models import Students

from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')

        s = Students(firstname=fname,email=email)
        s.save()
    return render(request, 'mysite/index.html')
