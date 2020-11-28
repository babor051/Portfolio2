from django.shortcuts import render
from home.models import Contact, Project

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):

    prjcts=Project.objects.all()

    return render(request, 'projects.html', {'prjcts': prjcts})


def contact(request):
    if request.method== 'POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        #print(name, email, phone, desc)
        ins= Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
    return render(request, 'contact.html')


