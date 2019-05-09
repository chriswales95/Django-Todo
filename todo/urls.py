from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item'),
    path('submit_new_item/', views.submit_new_item, name='submit_new_item'),
    path('completed_task/<int:item_id>/', views.completed_task, name='complete_task'),
]