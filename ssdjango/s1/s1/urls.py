from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ss/', include('ss.urls')),
    path('admin/', admin.site.urls)
]
