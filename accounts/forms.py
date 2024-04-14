from typing import Any
from django  import forms
from django.core.exceptions import FieldError
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phonenumber', 'fullname']
        kwargs = { "password": {
            "read_only": True}
        }
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        phonenumber = cleaned_data.get('phonenumber', None)
        
        if not phonenumber:
            raise forms.ValidationError({"phonenumber": "phonenumber us required"})
            
        if len(phonenumber) == 9:
            phonenumber = '998' + phonenumber
        
        if len(phonenumber) < 12 or not phonenumber:
            raise forms.ValidationError({"phonenumber": "Enter a valid phone number"})
        
        
        return cleaned_data