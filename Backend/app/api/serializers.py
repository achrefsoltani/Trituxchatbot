from rest_framework import serializers
from app.models import Choice,Chat,Message

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id',
                  'title_en','title_fr',
                  'response_fr','response_en',
                  'link_fr','link_en',
                  'next_choices','previous_choices'
                  ]

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
