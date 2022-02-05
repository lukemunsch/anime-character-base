from . import views
from django.urls import path


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path("<slug:slug>", views.CharacterDetail.as_view(), name="character_detail"),
    path('like/<slug:slug>', views.CharacterLike.as_view(), name='character_like'),
]
