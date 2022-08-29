from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Question
        fields = ['id', 'owner', 'question', 'detail', 'profile_id', 'created', 'updated', 'is_owner']