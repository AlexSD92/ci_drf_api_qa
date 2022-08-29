from django.urls import path
from upvotes import views


urlpatterns = [
    path('', views.ListUpvote.as_view()),
    path('<int:pk>/', views.DetailUpvote.as_view()),
]