from core.models import Project, Task
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # my_name = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()
    creator_id = serializers.IntegerField(write_only=True)
    tasks_count = serializers.IntegerField(default=0)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator_name', 'creator_id', 'tasks_count')

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.first_name
        return ''


class TaskSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # my_name = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()
    creator_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = '__all__'


