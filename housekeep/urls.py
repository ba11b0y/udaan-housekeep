from django.conf.urls import url
from django.urls import  path
from housekeep.views import AddAsset, AllAssets, AddWorker, AddTask, AllocateTask, TasksByWorker

urlpatterns = [
    url(r'add-asset/', AddAsset.as_view()),
    url(r'add-task/', AddTask.as_view()),
    url(r'add-worker/', AddWorker.as_view()),
    url(r'assets/all', AllAssets.as_view()),
    url(r'allocate-task/', AllocateTask.as_view()),
    path('get-tasks-for-worker/<int:wid>/', TasksByWorker.as_view()),
]