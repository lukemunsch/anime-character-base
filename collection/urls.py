from . import views
from django.urls import path


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('edit/<series_id>/', views.edit_series, name='edit_series'),
    path('series_list/', views.SeriesList.as_view(), name='series_list'),
    path('delete/<series_id>/', views.delete_series_req, name='delete_series'),
    path('create_character/', views.create_char, name='create_character'),
    path('update/<slug:slug>/', views.edit_char, name='edit_char'),
    path('create_series/', views.create_series, name='create_series'),
    path('create_suggestion/', views.create_sug, name='create_suggestion'),
    path('suggestions/', views.SuggestionList.as_view(), name='suggestions'),
    path('<slug:slug>/', views.CharacterDetail.as_view(), name='character_detail'),
]
