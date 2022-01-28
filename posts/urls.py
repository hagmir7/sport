from django.urls import path
from .views import *


urlpatterns = [
    path('post<slug:slug>', post, name='post'),
    path('create-post', createPost, name='create_post'),
    path('update-post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('privecy-policy', privecy, name='privecy'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('dashboard', dashboard, name='dashboard')
]