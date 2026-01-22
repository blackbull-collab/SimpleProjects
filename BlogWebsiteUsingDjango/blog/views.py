import logging
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm, ForgotPasswordForm, LoginForm, PostForm,RegisterForm, ResetPasswordForm
from .models import AboutUs, category, post
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail


# Create your views here.
#THIS IS STATIC DEMO DATA

# posts=[
#         {'id':1,'title':'post 1','content':'content of post 1'},
#         {'id':2,'title':'post 2','content':'content of post 2'},
#         {'id':3,'title':'post 3','content':'content of post 3'},
#         {'id':4,'title':'post 4','content':'content of post 4'}
#     ]

def index(request):
    blog_title="Latest posts"

    posts=post.objects.all()

    paginator=Paginator(posts,5)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)

    return render(request,'blog/index.html',{"blog_title":blog_title,"page_object":page_object})

def detail(request,slug):
    # post=next((item for item in posts if item['id']==int(post_id)),None)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f"post varaibale id {post}")
    
    #Getting data from model by post id
    try:
        post_id=post.objects.get(slug=slug)
        related_posts=post.objects.filter(category=post_id.category).exclude(pk=post_id.id)
    
    except post.DoesNotExist:
        raise Http404("Post Does not exist")
    
    return render(request,'blog/detail.html',{"post_id":post_id,"related_posts":related_posts})

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)

        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        logger=logging.getLogger("TESTING")

        if form.is_valid():
            logger.debug(f"post Data is { form.cleaned_data["name"]} { form.cleaned_data["email"]} { form.cleaned_data["message"]}")
            success_message="You email has been sent"
            #Send email or save in database codes here
            return render(request,'blog/contact.html',{"form":form,"success_message":success_message})
        else:
            logger.debug("Form validation Failure")

        return render(request,'blog/contact.html',{"form":form,"name":name,"email":email,"message":message})
    return render(request,'blog/contact.html')


def about(request):
    about_content=AboutUs.objects.first()

    if about_content is None or not about_content.content:
        about_content="Default content goes here if in database no content"
    
    else:
        about_content=about_content.content

    return render(request,"blog/about.html",{"about_content":about_content})


def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False) #THIS LINE WILL NOT CREATE DATA IN DATABASE FORST IT WILL RETURN TO THIS BCAZ coomit=false
            user.set_password(form.cleaned_data["password"])
            user.save() #user data created
            messages.success(request,"Registration Successfull. You can log in now ")
            return redirect("blog:login")

    return render(request,"blog/register.html",{"form":form})


def login(request):
    form=LoginForm()

    if request.method=="POST":
        form=LoginForm(request.POST)

        if form.is_valid():

            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)

            if user is not None:
                auth_login(request,user)
                print("Login Success !!!")
                return redirect("blog:dashboard")  #Redirecting to dashboard

    return render(request,"blog/login.html",{"form":form})


def dashboard(request):
    blog_title="My posts"

    #Getting user posts 
    all_posts=post.objects.filter(user=request.user)
    

    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)

    return render(request,"blog/dashboard.html",{"blog_title":blog_title,"page_object":page_object})


def logout(request):
    auth_logout(request)


def forgot_password(request):
    form=ForgotPasswordForm()

    if request.method=="POST":
        form=ForgotPasswordForm(request.POST)

        if form.is_valid():
            email=form.cleaned_data["email"]
            user=User.objects.get(email=email)

            #sending email to reset password 
            token=default_token_generator.make_token(user)
            u_id=urlsafe_base64_encode(force_bytes(user.pk))  #Sending user's primary key
            current_site=get_current_site(request)
            domain=current_site.domain
            subject="Reset Password Requested"
            message=render_to_string('blog/reset_password_email.html',{
                "domain":domain,
                "uid":u_id,
                "token":token

            })

            send_mail(subject,message,"noreply@example.com",[email])
            messages.success(request,"Email has been sent")

    return render(request,"blog/forgot_password.html",{"form":form})


def reset_password(request,uidb64,token):

    form=ResetPasswordForm()

    if request.method=="POST":
        form=ResetPasswordForm(request.POST)

        if form.is_valid():
            new_password=form.cleaned_data["new_password"]

            try:
                uid=urlsafe_base64_decode(uidb64)
                user=User.objects.get(pk=uid)
            except(TypeError,ValueError,OverflowError,User.DoesNotExist):
                user=None

            if user is not None and default_token_generator.check_token(user,token):
                user.set_password(new_password) #Password Hashing
                user.save()
                messages.success(request,"your password has been reset successfully !")
                return redirect("blog:login")
            else:
                messages.error(request,"The password reset link is invalid")
    return render(request,"blog/reset_password.html",{"form":form})


def new_post(request):

    categories=category.objects.all()

    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)

        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect("blog:dashboard")
    else:
        form=PostForm()
    return render(request,"blog/new_post.html",{"categories":categories,"form":form})


def edit_post(request,post_id):

    categories=category.objects.all()
    Post=get_object_or_404(post,id=post_id)

    if request.method=="POST":
        form=PostForm(request.POST,request.FILES,instance=Post)

        if form.is_valid():
            form.save()
            return redirect("blog:dashboard")
        
    else:
        form=PostForm()
        
    return render(request,"blog/edit_post.html",{"categories":categories})
