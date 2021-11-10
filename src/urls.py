from django.contrib import admin
from django.urls import path
from footfalls.views import dashboard_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_home, name='dashboard-home'),
]
