from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile, Project
from .utils import extract_text_from_pdf, match_projects, fetch_real_time_jobs, fetch_open_source_projects, get_courses, extract_skills

# Login View
def user_login(request):
    # Ensures login is prompted every time by logging out and clearing session data
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()  # Clears the session data

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:  # Ensure user is active
            login(request, user)
            return redirect('create_profile')  
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})

    return render(request, 'core/login.html')

# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            return redirect('create_profile')  # Redirect to profile creation
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# Create Profile View
@login_required
def create_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        is_update = True
    except UserProfile.DoesNotExist:
        user_profile = None
        is_update = False

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            if 'resume' in request.FILES:
                resume_text = extract_text_from_pdf(request.FILES['resume'])
                skills = extract_skills(resume_text)
                profile.skills = ", ".join(skills)
            else:
                skills = extract_skills(form.cleaned_data.get('skills', ''))
                profile.skills = ", ".join(skills)

            profile.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'core/create_profile.html', {'form': form, 'is_update': is_update})

# Dashboard View
@login_required
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    projects = Project.objects.all()
    real_time_jobs = fetch_real_time_jobs(user_profile.skills)
    open_source_projects = fetch_open_source_projects(user_profile.skills)
    courses = get_courses(user_profile.skills)  # Now using static course data

    # **Fixing the job data format before passing to template**
    formatted_jobs = []
    for job in real_time_jobs:
        formatted_jobs.append({
            "title": job.get("title", "Unknown Job"),
            "company_name": job.get("company", {}).get("display_name", "Unknown Company"),
            "location_name": job.get("location", {}).get("display_name", "Unknown Location"),
            "description": job.get("description", "No description available"),
            "redirect_url": job.get("redirect_url", "#"),
        })

    return render(request, 'core/dashboard.html', {
        'projects': projects,
        'jobs': formatted_jobs,
        'open_source_projects': open_source_projects,
        'courses': courses,
    })