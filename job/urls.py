from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    path('applied-jobs/', views.applied_jobs, name='applied-jobs'),
    path('shortlist_applicant/<int:job_pk>/<int:applicant_pk>/', views.shortlist_applicant, name='shortlist_applicant'),
    path('shortlisted-applicants/<int:job_pk>/', views.shortlisted_applicants, name='shortlisted-applicants'),
    path('remove-from-shortlist/<int:job_pk>/<int:applicant_pk>/', views.remove_from_shortlist, name='remove_from_shortlist'),

]