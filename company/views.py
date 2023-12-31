from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company
from .form import UpdateCompanyForm
from users.models import User
from django.shortcuts import render, get_object_or_404
from job.models import Job


@login_required
def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateCompanyForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info(request, 'Your company info has been updated!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
        else:
            form = UpdateCompanyForm(instance=company)
            context = {'form':form}
            return render(request, 'company/update_company.html', context)
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')

# view company details

def company_details(request, pk):
    company = get_object_or_404(Company, pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html', context)

def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)
    company = job.company  # Assuming 'company' is a ForeignKey in your Job model
    context = {'job': job, 'company': company}
    return render(request, 'website/job_details.html', context)
