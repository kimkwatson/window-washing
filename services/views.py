from django.shortcuts import render

def home(request):
    return render(request, 'services/home.html')

def request_service(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        return render(request, 'services/confirmation.html', {'name': name})
    
    return render(request, 'services/request_service.html')