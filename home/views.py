from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request): 
    latestPosts = Post.objects.all()
    numberOfPost=len(latestPosts)
    latestPosts=latestPosts[numberOfPost-2:]
    print(numberOfPost)
    return render(request,'home/home.html',{'latestPosts':latestPosts})

def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        content=request.POST.get('content','')
        if(len(name)<3 and len(email)<6 and len(phone)<10 and len(content)<5):
            messages.error(request,'Enter relevant data')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Thanks for contacting us')
    return render(request,'home/contact.html')

def about(request): 
    return render(request,'home/about.html')


def search(request): 
    search=request.GET.get('search','')
    if len(search)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=search)
        allPostsAuthor= Post.objects.filter(author__icontains=search)
        allPostsContent =Post.objects.filter(content__icontains=search)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': search}
    return render(request,'home/search.html',params)


def signup(request):
    if(request.method=='POST'):
        username=request.POST.get('username','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        myuser=authenticate(username=username,password=pass1)
        if(myuser is not None):
            messages.error(request, "Username or password already exists")
            return redirect('home')

        if(len(username)>10):
            messages.error(request, "Username too long. Enter at most 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')

        # Create an authenticate user

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')


    return HttpResponse("404 : Not Found")

def Login(request):
    if(request.method=='POST'):
        logusername=request.POST.get('logusername','')
        password=request.POST.get('password','')
        myuser=authenticate(username=logusername,password=password)
        if(myuser is not None):
            login(request,myuser)
            messages.success(request, " Welcome to Blogger")
            return redirect('home')
        else:
            messages.error(request, " Sorry, login failed")
            return redirect('home')
    return HttpResponse("404 : Not Found")


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')