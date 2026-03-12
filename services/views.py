from django.shortcuts import render
from .forms import ServiceRequestForm

def home(request):
    return render(request, 'services/home.html')

def request_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'services/confirmation.html', {'data': data})
    else:
        form = ServiceRequestForm

    return render(request, 'services/request_service.html', {'form': form})