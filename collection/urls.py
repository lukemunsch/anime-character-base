from . import views
from django.urls import path


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('series_list/', views.SeriesList.as_view(), name='series_list'),
    path('create_character/', views.create_character, name='create_character'),
    path('<slug:slug>', views.CharacterDetail.as_view(), name='character_detail'),
]
