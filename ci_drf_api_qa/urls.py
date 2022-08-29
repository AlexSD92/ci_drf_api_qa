from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', root_route),
    path('profiles/', include('profiles.urls')),
    path('questions/', include('questions.urls')),
    path('answers/', include('answers.urls')),
    path('upvotes/', include('upvotes.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
