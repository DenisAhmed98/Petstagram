from django.urls import path, include

from petstagram.pets import views

urlpatterns = (
    path('add/', views.add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details, name='pet_details'),
        path('edit/', views.pet_edit, name='pet_edit'),
        path('delete/', views.pet_delete, name='pet_delete'),
    ]))
)