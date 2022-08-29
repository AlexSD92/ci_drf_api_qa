from .models import Upvote
from .serializers import UpvoteSerializer
from rest_framework import permissions, generics
from ci_drf_api_qa.permissions import IsOwner


class ListUpvote(generics.ListCreateAPIView):
    serializer_class = UpvoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Upvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailUpvote(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    serializer_class = UpvoteSerializer
    queryset = Upvote.objects.all()