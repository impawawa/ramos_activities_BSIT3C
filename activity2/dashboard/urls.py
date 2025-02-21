from django.urls import path
from .views import index, report_view, settings_view

app_name = "dashboard"

urlpatterns = [
    path('', index, name='index'),   # This makes "/" work
    path('dashboard/', index, name='dashboard'),  # Keep this for direct dashboard access
    path('report/', report_view, name='report'),  # Ensure this matches 'report'
    path('settings/', settings_view, name='settings'),
]
