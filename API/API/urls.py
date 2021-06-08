from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('actual_api/', include('actual_api.urls')),
    path('admin/', admin.site.urls),
]