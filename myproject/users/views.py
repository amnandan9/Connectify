from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from jobs.models import Application

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('job_list')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('job_list')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.skills = request.POST.get('skills')
        profile.bio = request.POST.get('bio')

        if request.FILES.get('resume'):
            profile.resume = request.FILES['resume']

        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        return redirect('profile')

    return render(request, 'edit_profile.html', {'profile': profile})

@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': applications})