from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['Model', 'name', 'Option1', 'Option2', 'Option3', 'Option4']


