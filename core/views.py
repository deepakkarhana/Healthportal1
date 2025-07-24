from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Appointment
from .forms import AppointmentForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registration
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    query = request.GET.get('q')
    if query:
        doctors = doctors.filter(specialization__icontains=query) | doctors.filter(name__icontains=query)
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Link appointment to logged-in user
            appointment.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def success(request):
    return render(request, 'success.html')

@login_required
def profile(request):
    today = timezone.now().date()
    appointments = Appointment.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'auth/profile.html', {
        'appointments': appointments,
        'today': today
    })
def custom_logout(request):
    logout(request)
    return redirect('home')