from django.contrib import admin
from django import forms
from .models import Question

class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ['slug', 'created', 'last_updated', 'Model', 'name', 'Option1', 'Option2', 'Option3', 'Option4']
    #readonly_fields = ['slug', 'created', 'last_updated', 'Model', 'name', 'Option1', 'Option2', 'Option3', 'Option4']

admin.site.register(Question, QuestionAdmin)


