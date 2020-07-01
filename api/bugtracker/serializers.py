from rest_framework import serializers

from .models import Project, Issue


class IssueSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('id',)
        model = Issue


class ProjectSerializer(serializers.ModelSerializer):
    issue = IssueSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('id',)
        model = Project

    def to_representation(self, instance):
        rep = super(ProjectSerializer, self).to_representation(instance)
        rep['name'] = instance.user.name
        return rep
