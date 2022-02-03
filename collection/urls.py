from . import views
from django.urls import path


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home')
]
