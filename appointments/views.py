from django.shortcuts import render, redirect
from .models import Appointment, Barber
from django.http import HttpResponse
from django.contrib import messages

# def index(request):
#     barbers = Barber.objects.all()
#     return render(request, 'appointments/index.html', {'barbers': barbers})
from datetime import datetime

def index(request):
    barbers = Barber.objects.all()
    context = {
        'barbers': barbers,
        'year': datetime.now().year,
    }
    return render(request, 'appointments/index.html', context)


def book_appointment(request):

    if request.method == "POST":
        barber_id = request.POST['barber']
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        date = request.POST['date']
        time = request.POST['time']

        # Retrieve the selected barber and create an appointment
        barber = Barber.objects.get(id=barber_id)
        Appointment.objects.create(
            barber=barber,
            customer_name=customer_name,
            customer_email=customer_email,
            date=date,
            time=time
        )

        # Add a success message
        messages.success(request, "Appointment booked successfully!")

        # Redirect to the main page (change 'main_page' to your URL name for the homepage)
        return redirect('all_appointments')
    else:
        barbers = Barber.objects.all()
        return render(request, 'appointments/book.html', {'barbers': barbers})


def all_appointments(request):
    appointments = Appointment.objects.all()  # Get all appointments
    return render(request, 'appointments/all_appointments.html', {'appointments': appointments})