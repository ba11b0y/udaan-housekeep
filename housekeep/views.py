import datetime

from django.http import JsonResponse
from .models import Asset, Worker, Task
from rest_framework.views import APIView
from .serializers import AssetSerializer, WorkerSerializer, TaskSerializer


# Create your views here.


class AddAsset(APIView):

    def post(self, request):
        name = request.data["name"]
        asset = Asset(name=name)
        asset.save()
        return JsonResponse({"res": "Asset created successfully"})


class AddWorker(APIView):

    def post(self, request):
        name = request.data["name"]
        worker = Worker(name=name)
        worker.save()
        return JsonResponse(WorkerSerializer(worker).data)


class AllAssets(APIView):

    def get(self, request):
        assets = Asset.objects.all()
        json_data = AssetSerializer(assets, many=True).data
        return JsonResponse(json_data, safe=False)


class AddTask(APIView):

    def post(self, request):
        name = request.data["name"]
        freq = request.data["freq"]
        task = Task(name=name, frequency=freq)
        task.save()
        return JsonResponse(TaskSerializer(task).data, safe=False)


class AllocateTask(APIView):

    def post(self, request):
        asset_id = int(request.data["assetId"])
        task_id = int(request.data["taskId"])
        worker_id = int(request.data["workerId"])
        allocation_time = request.data["timeOfAllocation"]
        time_perform = request.data["taskToBePerformedBy"]
        task = Task.objects.get(pk=task_id)
        asset = Asset.objects.get(pk=asset_id)
        worker = Worker.objects.get(pk=worker_id)
        task.asset = asset
        task.worker = worker
        task.next_occurring_date = datetime.datetime.strptime(allocation_time, '%Y-%m-%d %H:%M:%S')
        task.date_to_be_performed_by = datetime.datetime.strptime(time_perform, '%Y-%m-%d %H:%M:%S')
        task.save()

        return JsonResponse(TaskSerializer(task).data, safe=False)


class TasksByWorker(APIView):

    def get(self, request, wid):
        worker = Worker.objects.get(pk=wid)
        tasks = Task.objects.filter(worker=worker)
        json_data = TaskSerializer(tasks, many=True).data
        return JsonResponse(json_data, safe=False)
