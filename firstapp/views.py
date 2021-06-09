from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User,auth
from django.urls import reverse
# Create your views here.

def home(request):
    categories = Category.objects.all()
    divisions = Division.objects.all()
    context={
        'categories':categories,
        'divisions':divisions,
    }
    return render(request,'index.html',context)

def products(request):
    
    prods = Advertisement.objects.all()
    
    return render(request,'products.html',{'products':prods})

def postadd(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            prod = AdvertisementForm(request.POST,request.FILES)
            
            if prod.is_valid():
                print(prod.cleaned_data['Books_Condition'])
                prod.save()
                return redirect('products')
            else:
                print("Invalid form")
                return redirect('postadd')
        else:
            #form = AdvertisementForm()
            categories=Category.objects.all()
            return render(request,'postadd.html',{'categories':categories})
    else:
        return redirect('login')

def showdetails(request,id):
    prod = Advertisement.objects.get(id = id)
    if prod is not None:
        return render(request,'showdetails.html',{'product':prod})
    return render(request,'products.html')
    #return render(request,'showdetails.html')
    
def profile(request):
    if request.user.is_authenticated:
        if Profile.objects.filter(User = request.user).exists():
            profile = Profile.objects.get(User = request.user)
            return render(request,'profile.html',{'profile':profile})
        print("profile nai, aage bana")
        return redirect('profilesetup')
    else:
        return redirect('login')
    
def profilesetup(request):
    if request.user.is_authenticated:
        if Profile.objects.filter(User = request.user).exists():
            return redirect('profile')
        if request.method == "POST":
            profile = ProfileForm(request.POST,request.FILES)
            if profile.is_valid():
                profile.save()
                return redirect('profile')
            print("form invalid")
            return redirect('profilesetup')
        
        divisions = Division.objects.all()
        districts = District.objects.all()
        context = {
            'divisions': divisions,
            'districts': districts,
        }
        return render(request,'profilesetup.html',context)
    
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            email = request.POST['Email']
            password = request.POST['Password']
            print(email,password)
            user = auth.authenticate(username = email,email = email, password = password)
            if user is None:
                print("invalid login")
                redirect('login')
            else:
                auth.login(request,user)
                print("okay login")
                return redirect('profile')
        return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = email
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print("username taken")
            else:
                user = User.objects.create_user(
                    username = username, email = email, password = password1, 
                    first_name = first_name, last_name = last_name
                    )
                user.save()
                return redirect('login')
        else:
            print("password didn't match")
            
        return redirect('register')

    return render(request,'register.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/')
    else:
        return redirect('login')
    
def managead(request):
    if request.user.is_authenticated:
        #prods = Advertisement.objects.get(username = request.user.username)
        prods = Advertisement.objects.filter(Poster = request.user)
        
        if prods is None:
            print("ad nai")
        else:
            print("ad ache")
        return render(request,'products.html',{'products':prods})
    else:
        return redirect('login')
    
def deletead(request,id):
    product = Advertisement.objects.get(id=id)
    product.delete()
    return redirect('managead')

def updatead(request,id):
    if request.method == "POST":
        prev = Advertisement.objects.get(id=id)
        prod = AdvertisementForm(request.POST,request.FILES,instance=prev)
        if prod.is_valid():
            prod.save()
            print("saved form")
            return redirect('showdetails',id=id)
        print("form invalid")
        return redirect('updatead')
    
    prod = Advertisement.objects.get(id=id)
    categories = Category.objects.all()
    context={
        'product':prod,
        'categories':categories,
    }
    return render(request,'updatead.html',context)

def products_cat(request,id):
    div = Division.objects.get(pk = id)
    prods = Advertisement.objects.filter(Division = div)
    return render(request,'products.html',{'products':prods})