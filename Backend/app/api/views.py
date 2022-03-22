from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import Choice
from .serializers import ChoiceSerializer

class ChoiceListApiView(APIView):

    def get(self,request,id=None):
        if id:
            choice = Choice.objects.get(id=id)
            serializer = ChoiceSerializer(choice)
            return Response(serializer.data, status=status.HTTP_200_OK)

        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


