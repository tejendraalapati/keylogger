from django.shortcuts import render, redirect
from .models import KeystrokeLog

def record_keystroke(request):
    if request.method == 'POST':
        key_pressed = request.POST.get('key_pressed')
        KeystrokeLog.objects.create(key_pressed=key_pressed)
        return redirect('view_logs')
    return render(request, 'record_keystroke.html')

def view_logs(request):
    logs = KeystrokeLog.objects.all()
    return render(request, 'view_logs.html', {'logs': logs})