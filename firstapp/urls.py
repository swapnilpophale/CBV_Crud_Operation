from django.urls import path
from .views import *

urlpatterns = [
    path('', Homeview.as_view(), name='studentcreate'),
    path('studentlist/', StudentListView.as_view(), name='studentlist'),
    path('studentupdate/<int:pk>', StudentUpdateView.as_view(), name='studentupdate'),
    path('studentdelete/<int:pk>', StudentDeleteView.as_view(), name='studentdelete'),
    path('updatesuccess/', SuccessUpdate.as_view(), name='success'),
]
