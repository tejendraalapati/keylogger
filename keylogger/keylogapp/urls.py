# keylogger_app/urls.py
from django.urls import path
from .views import record_keystroke, view_logs

urlpatterns = [
    path('', record_keystroke, name='record_keystroke'),
    path('logs/', view_logs, name='view_logs'),
]
