from . import models

from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'Model', 
            'name', 
            'Option1', 
            'Option2', 
            'Option3', 
            'Option4', 
        )


