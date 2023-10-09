from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bankwells/', include('bankwells.urls')),
    path('admin/', admin.site.urls),
]