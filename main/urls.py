from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.home, name='portfolio'),  # Remove this if you want a single page layout
    path('about/', views.home, name='about'),  # Remove this if you want a single page layout
    path('services/', views.home, name='services'),  # Remove this if you want a single page layout
    path('contact/', views.home, name='contact'),  # Remove this if you want a single page layout
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
     path('contact/submit/', views.contact_view, name='contact_submit'),
]
