from rest_framework.serializers import ModelSerializer
from .models import Asset, Worker, Task


class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = ('name', 'pk',)


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name', 'pk',)


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'frequency', 'pk',)
