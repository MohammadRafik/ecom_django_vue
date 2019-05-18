from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def submit_register(request):
    x = request.POST
    t=2
    return render(request, 'accounts/test.html')