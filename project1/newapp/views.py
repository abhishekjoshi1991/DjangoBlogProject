from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserRegistration, AddPost, EditProfile
from .models import Blog
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# Function for homepage
def homepage(request):
    all_data = Blog.objects.order_by('-id')
    return render(request, 'home.html',{'all':all_data,'home':'active'})

# Function for aboutpage
def about(request):
    return render(request, 'about.html',{'about':'active'})

# Function for user login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = AuthenticationForm()
        return render(request,'userlogin.html',{'form':form,'log':'active'})
    else:
        return HttpResponseRedirect('/dashboard/')

# Function to edit profile
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditProfile(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = EditProfile(instance = request.user)
        return render(request,'edit_profile.html',{'form':form})
    else:
        return HttpResponseRedirect('/userlogin/')

# Function for new user registration
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            form=UserRegistration()
            return HttpResponseRedirect('/userlogin/')
    else:
        form= UserRegistration()
    return render(request,'signup.html',{'form':form})

# Function for homepage
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            specific_data = Blog.objects.order_by('-id')
        else:
            specific_data = Blog.objects.filter(user_id_id = request.user.id).order_by('-id')
        return render(request, 'dashboard.html',{'specific_data':specific_data, 'dashboard':'active'})
    else:
        return HttpResponseRedirect('/userlogin/')

# Function to logout from session
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/userlogin/')

# Reset Password by entering the old password (Use PasswordChangeForm)
def resetpassword(request):
    if request.user.is_authenticated: #if user is authenticated then only he can change the password
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'passwordreset.html', {'form':form})
    else:
        return HttpResponseRedirect('/userlogin/')


# Function to add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddPost(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                tit = form.cleaned_data['title']
                desc = form.cleaned_data['description']
                modelobj = Blog(user_id=user, title=tit, description =desc)
                modelobj.save()
                messages.success(request, 'New post has been added successfully')
                # OR
                # blog = Blog()
                # blog.user_id = user
                # blog.title = tit
                # blog.description = desc
                # blog.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = AddPost()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/userlogin/')
    
# Function to Edit Post
def edit_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            blog_edit = Blog.objects.get(pk=id) #get data for specific id and then pass it as instance below
            form = AddPost(request.POST, instance=blog_edit)
            if form.is_valid():
                form.save()
                form = AddPost()
                messages.success(request, 'Post has been edited successfully')
                return HttpResponseRedirect('/dashboard/')
        else: #if method is GET then
            blog_edit = Blog.objects.get(pk=id)
            form = AddPost(instance=blog_edit) #display form with instance data
        return render(request,'editpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/userlogin/')

# Function to delete the Post
def delete_post(request,id):
    if request.user.is_authenticated:
        blog_delete = Blog.objects.get(pk=id)
        blog_delete.delete()
        messages.error(request,'Post Deleted Successfully')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/userlogin/')


