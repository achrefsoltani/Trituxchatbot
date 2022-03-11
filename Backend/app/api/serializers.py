from rest_framework import serializers
from app.models import Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['title_en','title_fr']
