from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
 

    path('', views.WorkersList.as_view(), name='worker-list'),
    path('create/', views.WorkerCreateView.as_view(), name='worker-create'),
    path('<pk>/', views.WorkerDetail.as_view(), name='worker-detail'),
    path('<pk>/update/', views.WorkerUpdate.as_view(), name='worker-update'),
    path('<pk>/delete/', views.WorkerDelete.as_view(), name='worker-delete'),


 
]