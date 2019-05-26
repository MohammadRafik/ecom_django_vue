from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model

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
            # logging the user in since hes registration is successful
            user = authenticate(username=form.cleaned_data['username'], password =form.cleaned_data['password'])
            login(request, user)
            return redirect('accounts')
        else:
            return render(request, self.template_name, {'form':form})

class Login(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        User = get_user_model()
        if '@' in username:
            try:
                current_user = User.objects.get(email__iexact=username)
                username = current_user.username
            except:
                error = "Oops! something's wrong. We couldn't find that email"
                return render(request, self.template_name, {'error':error, 'form_username':username})

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts')
        else:
            error = "Oops! something's wrong. Your username/email and password didnt match"
            return render(request, self.template_name,  {'error':error, 'form_username':username})
