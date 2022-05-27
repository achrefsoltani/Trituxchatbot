from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import Choice
from .serializers import ChoiceSerializer,ChatSerializer,MessageSerializer

class ChoiceListApiView(APIView):
    """
    List all choices or retrieve choice based on id
    """

    def get(self,request,id=None):
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
    def post(self,request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageApiView(APIView):
    """
    Create New Message Instance
    """
    def post(self,request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['content'])
            if (serializer.data['content']) :
                return Response(serializer.data['content'], status=status.HTTP_200_OK)
            else :
                return Response(serializer.data, status=status.HTTP_200_OK)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


