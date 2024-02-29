from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('questions/', include('apps.questions.urls')),
    path('admin/', admin.site.urls),
]