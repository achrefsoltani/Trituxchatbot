from rest_framework import serializers
from app.models import Choice, Chat, Message, Client, ContactRequest, DemoRequest, Demo


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id',
                  'title_en', 'title_fr',
                  'response_fr', 'response_en',
                  'link_fr', 'link_en',
                  'next_choices', 'previous_choices'
                  ]


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ContactRequestSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ContactRequest
        fields = '__all__'

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        try:
            client = Client.objects.get(email=client_data.get('email'))
        except Client.DoesNotExist:
            client = Client.objects.create(**client_data)

        instance = ContactRequest.objects.create(**validated_data)
        instance.client = client
        instance.status = "unclaimed"
        instance.save()
        return instance


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'


class DemoRequestSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    demo = DemoSerializer()

    class Meta:
        model = DemoRequest
        fields = '__all__'

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        demo_data = validated_data.pop('demo')
        try:
            client = Client.objects.get(email=client_data.get('email'))
        except Client.DoesNotExist:
            client = Client.objects.create(**client_data)

        try:
            demo = Demo.objects.get(event_id=demo_data.get('event_id'))
        except Demo.DoesNotExist:
            demo = Demo.objects.create(**demo_data)

        instance = DemoRequest.objects.create(**validated_data)
        instance.client = client
        instance.demo = demo
        instance.save()
        return instance
