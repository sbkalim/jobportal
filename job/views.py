from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm
from users.models import User


# create a job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form =  CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New job has been created')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your job info is updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form':form}
        return render(request, 'job/update_job.html', context)


def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)


# def apply_to_job(request, pk):
#     if request.user.is_authenticated and request.user.is_applicant:
#         if request.user.has_resume:
#             job = Job.objects.get(pk=pk)
#             if ApplyJob.objects.filter(user=request.user, job=pk).exists():
#                 messages.warning(request, 'Permission Denied')
#                 return redirect('dashboard')
#             else:
#                 ApplyJob.objects.create(
#                     job=job,
#                     user = request.user,
#                     status = 'Pending'
#                 )
#                 messages.info(request, 'You have successfully applied! Please see dashboard')
#                 return redirect('dashboard')
#         else:
#             messages.warning(request, 'Permission denied. Please create a resume')
#             return redirect('dashboard')
#     else:
#         messages.info(request, 'Please log in to continue')
#         return redirect('logout')

def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        if request.user.has_resume:
            job = Job.objects.get(pk=pk)
            if ApplyJob.objects.filter(user=request.user, job=pk).exists():
                messages.warning(request, 'Permission Denied')
                return redirect('dashboard')
            else:
                shortlisted = request.POST.get('shortlisted')  # Get the value of the checkbox
                ApplyJob.objects.create(
                    job=job,
                    user=request.user,
                    status='Pending',
                    shortlisted=shortlisted == 'on'  # Convert checkbox value to boolean
                )
                messages.info(request, 'You have successfully applied! Please see dashboard')
                return redirect('dashboard')
        else:
            messages.warning(request, 'Permission denied. Please create a resume')
            return redirect('dashboard')
    else:
        messages.info(request, 'Please log in to continue')
        return redirect('logout')




def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.select_related('user').all()  # Select related to fetch related user data
    context = {'job': job, 'applicants': applicants}
    return render(request, 'job/all_applicants.html', context)

def shortlist_applicant(request, job_pk, applicant_pk):
    job = Job.objects.get(pk=job_pk)
    applicant = User.objects.get(pk=applicant_pk)
    apply_job = ApplyJob.objects.get(job=job, user=applicant)
    apply_job.shortlisted = True
    apply_job.save()
    messages.info(request, f'{applicant.username} has been shortlisted.')
    return redirect('all-applicants', pk=job.pk)


def shortlisted_applicants(request, job_pk):
    job = Job.objects.get(pk=job_pk)
    shortlisted_applicants = ApplyJob.objects.filter(job=job, shortlisted=True)
    context = {'job': job, 'shortlisted_applicants': shortlisted_applicants}
    return render(request, 'job/shortlisted_applicants.html', context)



def remove_from_shortlist(request, job_pk, applicant_pk):
    job = Job.objects.get(pk=job_pk)
    applicant = User.objects.get(pk=applicant_pk)
    apply_job = ApplyJob.objects.get(job=job, user=applicant)
    apply_job.shortlisted = False  # Remove from shortlist
    apply_job.save()
    messages.info(request, f'{applicant.username} removed from shortlist.')
    return redirect('shortlisted-applicants', job_pk=job.pk)



def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request, 'job/applied_job.html', context)