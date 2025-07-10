from django import forms
from app.models import *

class TopicForm(forms.Form):
    tname=forms.CharField()



class WebpageForm(forms.Form):
    tname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

