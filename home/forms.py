from django import forms

class PostForm(forms.Form):
    photo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)