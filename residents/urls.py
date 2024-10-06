from django.urls import path
from . import views

urlpatterns = [
    path('', views.resident_list, name='resident_list'),
    path('<int:pk>/', views.resident_detail, name='resident_detail'),
    path('create/', views.resident_create, name='resident_create'),
    path('<int:pk>/edit/', views.resident_update, name='resident_update'),
    path('<int:pk>/delete/', views.resident_delete, name='resident_delete'),
    #path('residents/<int:resident_id>/add_medication_entry/', views.add_medication_entry, name='add_medication_entry'),
    path('residents/<int:resident_id>/add_medication/', views.add_medication_entry, name='add_medication_entry'),
    path('residents/<int:pk>/', views.resident_detail, name='resident_detail'),
    path('medication_entry/<int:entry_id>/edit/', views.edit_medication_entry, name='edit_medication_entry'),
    path('medication_entry/<int:entry_id>/delete/', views.delete_medication_entry, name='delete_medication_entry'),
    #path('', views.index, name='index'), #strona główna
]
