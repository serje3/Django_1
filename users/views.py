from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,authenticate, login
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    user = authenticate(request,username=request.POST['username'],password=request.POST['password'])

    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('learning_logs:index'))
    else:
        return render(request,'learning_logs/index.html',context={'login':False})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)