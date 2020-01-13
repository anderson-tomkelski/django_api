from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContentList(APIView):
    def get(self, request, format=None):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)