from dataclasses import field
from django import forms

from .models import contact, SubscriptionEmail


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'


class SubscriptionEmailForm(forms.ModelForm):
    subsrcip_mail = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "emails are good start....",
                "class": "form-control",
                "style" : "border: none;",
            }
        ),
        label="",
    )
    class Meta:
        model = SubscriptionEmail
        exclude = ('subemail', )
