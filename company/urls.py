from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update-company/', views.update_company, name='update-company'),
    path('company-details/<int:pk>/', views.company_details, name='company-details')
    # path('company-details/', views.company_details, name='company-details')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)