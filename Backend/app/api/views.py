import datetime
import json

from app.api.calendar import update_event

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import Choice, Message
from .serializers import ChoiceSerializer, ChatSerializer, MessageSerializer, ContactRequestSerializer, \
    DemoRequestSerializer
from app.api.calendar import list_events


class ChoiceListApiView(APIView):
    """
    List all choices or retrieve choice based on id
    """

    def get(self, request, id=None):
        if id:
            choice = Choice.objects.get(id=id)
            serializer = ChoiceSerializer(choice)
            return Response(serializer.data, status=status.HTTP_200_OK)

        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChatApiView(APIView):
    """
    Create New Chat Instance
    """

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageApiView(APIView):
    """
    Create New Message Instance
    """

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if (serializer.data['content']):
                # Chatbot response function here / response need to be in message format
                response = Message(sender='chatbot',
                                   chat_id=serializer.data['chat'],
                                   type='text',
                                   content='received :' + serializer.data['content'],
                                   date=datetime.datetime.now())
                # Saving the response in Chat
                response.save()
                r = MessageSerializer(response)

                return Response(r.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactRequestApiView(APIView):
    """
    Create New ContactRequest and/or Client
    """

    def post(self, request):
        serializer = ContactRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DemoRequestApiView(APIView):

    # Get next 4 events for a specific service
    def get(self, request, id):
        calendarId = None
        if id == 1:
            calendarId = '9pnkofdjft4o57nlhi71oohbts@group.calendar.google.com'
        elif id == 2:
            calendarId = 'qkk3lcmogn69kc82jviqp4gnqs@group.calendar.google.com'
        elif id == 3:
            calendarId = 'evq2mpfdjsq600i2aqcgaudjq8@group.calendar.google.com'

        if calendarId:
            events = list_events(calendarId=calendarId)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Create New DemoRequest and/or Client

    def post(self, request):
        calendarId = None
        serializer = DemoRequestSerializer(data=request.data)
        if serializer.is_valid():
            id = request.data['demo']['service']
            if id == 1:
                calendarId = '9pnkofdjft4o57nlhi71oohbts@group.calendar.google.com'
            elif id == 2:
                calendarId = 'qkk3lcmogn69kc82jviqp4gnqs@group.calendar.google.com'
            elif id == 3:
                calendarId = 'evq2mpfdjsq600i2aqcgaudjq8@group.calendar.google.com'
            update_event(calendarId,request.data['demo']['event_id'],request.data['client']['email'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
