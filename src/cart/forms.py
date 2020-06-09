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


    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)

        # here we just change the secondary address field so that it wont be required by the frontend
        self.fields['secondary_address'].required = False


