from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from django.http import Http404
from rest_framework import status, permissions
from ci_drf_api_qa.permissions import IsOwner


class ListQuestion(APIView):
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )