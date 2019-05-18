from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def submit_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/auth/user')

    else:
        form = RegistrationForm()

        args = { 'form': form }
        return render(request, 'accounts/register.html', args)
