from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
