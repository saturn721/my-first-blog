from django import forms
from .models import Ordering

class OrderingForm(forms.ModelForm):

    class Meta:
        model = Ordering
        fields = ('author', 'email', 'title', 'text',)