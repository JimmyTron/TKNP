from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import StudentRegistrationForm, StudentUpdateForm, ProfileUpdateForm
from .models import *
from clearance.models import Department, Subject, Request

def home(request):
    clearance=Request(request)
    context = {
        'title': 'Clearance Home',
        'status': clearance.status,
        'posts': Department.objects.all()
    }
    return render(request, 'students/home.html',context)

def docs(request):
    context = {
        'title': 'Documentation'
    }
    return render(request, 'students/documentation.html',context)

@login_required
def general(request):
    clearance=Request(request)
    context = {
        'title': 'General Clearance',
        'status': clearance.status,
        'posts': Department.objects.all()
    }
    return render(request, 'students/general.html',context)
   
@login_required
def departmental(request):
    clearance=Request(request)
    context = {
        'title': 'Departmental Clearance',
        'status': clearance.status,
        'posts': Subject.objects.all()
    }
    return render(request, 'students/departmental.html',context)

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            adm_no = form.cleaned_data.get('admission_number')
            username = form.cleaned_data.get('username')

            if Student.objects.filter(adm_no=adm_no).exists():
                with transaction.atomic():
                    student = Student.objects.get(adm_no=adm_no)
                    department = student.department
                    course = student.course
                    user = form.save()
                    profile = Profile.objects.create(user=user, department=department, course=course, Adm_no=adm_no)
                    
                    messages.success(request, f'Account created for {username}! You can now access the site.')
                    return redirect('students-login')
            else:
                messages.info(request, "Student with that admission number does not exist")
                return redirect('students-registration')
   
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form':form,'title':'Students Sign Up'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = StudentUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Profile')

    else:
        u_form = StudentUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'students/profile.html', context)
