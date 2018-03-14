from django import forms
from .models import Entering


class EnteringForm(forms.ModelForm):

    class Meta:
        model = Entering
        fields = ('token',)
