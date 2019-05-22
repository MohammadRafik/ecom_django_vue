from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.views import View

# Create your views here.
class Register(View):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')
        else:
            return render(request, self.template_name, {'form':form})


        