from rest_framework import serializers
from app.models import Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id',
                  'title_en','title_fr',
                  'response_fr','response_en',
                  'link_fr','link_en',
                  'next_choices','previous_choices'
                  ]
