from rest_framework import serializers
from .models import Upvote
from django.db import IntegrityError


class UpvoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Upvote
        fields = ['id', 'created', 'owner', 'question']

    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })