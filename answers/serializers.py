from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Answer
        fields = ['id', 'owner', 'question', 'answer', 'profile_id', 'created', 'updated', 'is_owner']


class AnswerDetailSerializer(AnswerSerializer):
    answer = serializers.ReadOnlyField(source='question.id')