from django.urls import path
from .views import home, details

urlpatterns = [
    path('', home, name='home'),
    path('<str:pk>/', details, name='project_details')
]