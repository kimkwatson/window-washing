from django.shortcuts import render
from .forms import ServiceRequestForm
from .models import ServiceRequest

# render homepage
def home(request):
    return render(request, 'services/home.html')

# handle displaying the form and processing submissions
def request_service(request):
    
    # if the form is submitted
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)

        # validate form data
        if form.is_valid():
            data = form.cleaned_data # cleaned and validated input

            # create and save a new ServiceRequest in the database
            saved_request = ServiceRequest.objects.create(
                fname=data['fname'],
                lname=data['lname'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                city=data['city'],
                state=data['state'],
                zip=data['zip'],
                stories=data['stories'],
                windows=data['windows'],
                service=data['service'],
                day=data['day'],
                notes=data['notes'],
            )
            
            # show confirmation page with saved data
            return render(request, 'services/confirmation.html', {'data': saved_request})
    else:
        # if not submitted yet, display an empty form
        form = ServiceRequestForm()

    # render the form page (either first load or with errors)
    return render(request, 'services/request_service.html', {'form': form})