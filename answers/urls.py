from django.urls import path
from answers import views


urlpatterns = [
    path('', views.ListAnswer.as_view()),
    path('<int:pk>/', views.DetailAnswer.as_view()),
]