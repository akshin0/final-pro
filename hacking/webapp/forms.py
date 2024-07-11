from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    fullname = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email = forms.EmailField(max_length=254, label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Subscriber
        fields = "__all__"