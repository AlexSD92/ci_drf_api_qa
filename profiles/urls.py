from django.urls import path
from profiles import views


urlpatterns = [
    path('', views.ListProfile.as_view()),
    path('<int:pk>/', views.DetailProfile.as_view()),
]