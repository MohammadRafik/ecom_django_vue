from django import forms
from cart.models import CheckoutDetails

class CheckoutForm(forms.ModelForm):

    class Meta:
        model = CheckoutDetails
        fields = [ 'name_of_receiver', 'main_address', 'secondary_address', 'city', 'province', 'postal_code', 'phone_number']
        widgets = {
            'name_of_receiver': forms.TextInput(attrs={'class': 'form-control'}),
            'main_address': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }

    # here we change one the fields so that it wont be required by the frontend
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CheckoutForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['secondary_address'].required = False





    # name_of_receiver = forms.CharField(max_length=100, label = 'receiver_name')
    # main_address = forms.CharField(max_length=200, label = 'main_address')
    # secondary_address = forms.CharField(max_length=100, label = 'secondary_address')
    # city = forms.CharField(max_length=100, label = 'city')
    # province = forms.CharField(max_length=20, label = 'province')
    # postal_code = forms.CharField(max_length=12, label = 'postal_code')
    # phone_number = forms.CharField(max_length=12, label = 'phone_number')
