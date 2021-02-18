# file ini dibuat untuk membuat form komentar
from django import forms


class CommentForm(forms.Form):
    # max_length harus sama dengan yang ada pada model
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    ) 
    