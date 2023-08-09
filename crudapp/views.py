from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

#To add and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()        
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    stud = User.objects.all()            
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

#To delete items:

def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=pi)
    return render(request,'enroll/update.html', {'form':fm})