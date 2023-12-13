from django.urls import path
from inventario import views

urlpatterns = [
    path('', views.ApiOverview.as_view(), name='api-overview'),
    path('create/', views.AddItems.as_view(), name='add-items'),
    path('all/', views.ViewItems.as_view(), name='view-items'),
    path('update/<int:pk>/', views.UpdateItems.as_view(), name='update-items'),
    path('item/<int:pk>/delete/', views.DeleteItems.as_view(), name='delete-items'),
]