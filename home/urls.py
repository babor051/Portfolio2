from django.contrib import admin
from django.urls import path, include
from home import views

# admin customization
admin.site.site_header="Login to Developer {Babor's} Admin Panel"
admin.site.site_title="{Babor's} Dashboard"
admin.site.index_title="Admin"

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
]
