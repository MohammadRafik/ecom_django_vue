from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def submit_register(request):
    return render(request, 'accounts/test.html')