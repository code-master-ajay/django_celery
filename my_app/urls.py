from django.urls import path
from .views import home


urlpatterns = [
    path('test/', home,name='home'),
]
