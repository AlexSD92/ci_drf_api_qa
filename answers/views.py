from .models import Answer
from .serializers import AnswerSerializer, AnswerDetailSerializer
from rest_framework import permissions, generics
from ci_drf_api_qa.permissions import IsOwner


class ListAnswer(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailAnswer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = AnswerDetailSerializer
    queryset = Answer.objects.all()