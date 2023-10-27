from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['trip', 'airline', 'departure_date', 'arrival_date', 'visa', 'visa_price', 'visa_duration']

    visa_price = forms.IntegerField(
        label='Visa Price (USD)',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 50', 'type': 'number', 'step': '1'}),
        min_value=0
    )

    visa_duration = forms.IntegerField(
        label='Visa Duration (in days)',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 30', 'type': 'number', 'step': '1'}),
        min_value=0
    )

    def clean_visa_price(self):
        visa_price = self.cleaned_data.get('visa_price')
        if visa_price is not None:
            if not isinstance(visa_price, int):
                raise forms.ValidationError("Visa Price should be an integer.")
        return visa_price

    def clean_visa_duration(self):
        visa_duration = self.cleaned_data.get('visa_duration')
        if visa_duration is not None:
            if not isinstance(visa_duration, int):
                raise forms.ValidationError("Visa Duration should be an integer.")
        return visa_duration