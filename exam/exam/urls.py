from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('exam.profiles.urls')),
    path('', include('exam.notes.urls')),
]
