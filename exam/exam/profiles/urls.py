from django.urls import path

from exam.profiles.views import profile_home, delete_profile

urlpatterns = [
    path('', profile_home, name='profile'),
    path('delete/', delete_profile, name='delete profile'),
]