from django.contrib import admin
from .models import Industry, State, ApplyJob, Job

admin.site.register(State)
admin.site.register(Industry)
admin.site.register(ApplyJob)
# admin.site.register(Job)