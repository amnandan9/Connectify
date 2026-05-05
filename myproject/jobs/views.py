from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from notifications.models import Notification

def job_list(request):
    query = request.GET.get('q')
    location = request.GET.get('location')

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)

    if location:
        jobs = jobs.filter(location__icontains=location)

    applied_jobs = []
    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(
            user=request.user
        ).values_list('job_id', flat=True)

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if Application.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, "Already applied!")
    else:
        Application.objects.create(user=request.user, job=job)

        Notification.objects.create(
            user=job.user,
            message=f"{request.user.username} applied to your job"
        )

        messages.success(request, "Application submitted!")

    return redirect('job_list')

