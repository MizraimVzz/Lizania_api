from django.urls import path
from users import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('token/', views.CreateTokenView.as_view()),
    path('user/<int:pk>/', views.ModifyUserView.as_view(), name='user-modify'),
    path('miembros/', views.MiembrosListView.as_view(), name='miembros-list'),
]