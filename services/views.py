from django.shortcuts import render
from .forms import ServiceRequestForm
from .models import ServiceRequest

def home(request):
    return render(request, 'services/home.html')

def request_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            ServiceRequest.objects.create(
                fname=data['fname'],
                lname=data['lname'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                city=data['city'],
                state=data['state'],
                zip=data['zip'],
                windows=data['windows'],
                service=data['service'],
                day=data['day'],
                notes=data['notes'],
            )
            
            return render(request, 'services/confirmation.html', {'data': data})
    else:
        form = ServiceRequestForm()

    return render(request, 'services/request_service.html', {'form': form})