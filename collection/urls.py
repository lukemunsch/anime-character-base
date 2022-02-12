from . import views
from django.urls import path


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('series_list/', views.SeriesList.as_view(), name='series_list'),
    path('create_character/', views.create_char, name='create_character'),
    path('edit/<char_id>', views.edit_char, name='edit_character'),
    path('create_series/', views.create_series, name='create_series'),
    path('create_suggestion/', views.create_sug, name='create_suggestion'),
    path('suggestions/', views.SuggestionList.as_view(), name='suggestions'),
    path('<slug:slug>/', views.CharacterDetail.as_view(), name='character_detail'),
]
