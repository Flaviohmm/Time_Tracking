from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Punch
from .forms import PunchForm, LoginForm
from django.contrib.auth.models import User
from datetime import datetime

@login_required
def punch(request):
    if request.method == 'POST':
        form = PunchForm(request.POST)
        if form.is_valid():
            punch = form.save(commit=False)
            punch.user = request.user
            punch.save()
            return redirect('attendance:report')
    else:
        form = PunchForm()
    return render(request, 'attendance/punch.html', {'form': form})

@login_required
def report(request):
    punches = Punch.objects.filter(user=request.user)
    context = {
        'daily_report': punches.filter(punch_in_time__date=datetime.now().date()),
        'weekly_report': punches.filter(punch_in_time__week=datetime.now().isocalendar()[1]),
        'monthly_report': punches.filter(punch_in_time__month=datetime.now().month)
    }
    return render(request, 'attendance/report.html', context)

def login_view(request):
    form = LoginForm()
    print(form)
    return render(request, 'login.html', {'form': form})
