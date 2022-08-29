from django.urls import path
from questions import views


urlpatterns = [
    path('', views.ListQuestion.as_view())
]