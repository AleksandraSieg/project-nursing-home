from django.urls import path
from . import views

urlpatterns = [
    path('', views.medication_list, name='medication_list'),
    path('<int:pk>/', views.medication_detail, name='medication_detail'),
    path('create/', views.medication_create, name='medication_create'),
    path('<int:pk>/edit/', views.medication_update, name='medication_update'),
    path('<int:pk>/delete/', views.medication_delete, name='medication_delete'),
]
