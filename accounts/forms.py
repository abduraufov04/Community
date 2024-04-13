from django.forms import ModelForm
from .models import CustomUser

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phonenumber', 'fullname']
        kwargs = { "password": {
            "read_only": True}
        }

    def validate_unique(self) -> None:
        print(11111111111, self)
        return super().validate_unique()
