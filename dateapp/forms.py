from django import forms
from .models import DateResponse

class DateResponseForm(forms.ModelForm):
    class Meta:
        model = DateResponse
        fields = ['response']
        widgets = {
            'response': forms.RadioSelect(choices=[('yes', 'Yes'), ('no', 'No')]),
        }