from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from seventh_app.forms import UserForms,UserInfoForms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,"seventh_app/First.html")

def register(request):
    registered=False

    if request.method == 'POST':
        a=UserForms(data=request.POST)
        b=UserInfoForms(data=request.POST)
        if a.is_valid() and b.is_valid():

            user = a.save()
            user.set_password(user.password)
            user.save()

            profile=b.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
        else :
            print(a.errors,b.errors)

    else :
        a = UserForms()
        b = UserInfoForms()
    my_dict=dict()
    my_dict['au']=a
    my_dict['bui']=b
    my_dict['regg'] = registered

    return render(request,'seventh_app/Registration.html',context=my_dict)

def user_login(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        user = authenticate(username=un,password=pswd)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else :
            return HttpResponse("account not active")
    else:
        return render(request,'seventh_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


