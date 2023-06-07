from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.PokemonRetrieveAPIView.as_view()),
    path('create', views.PokemonListCreateAPIView.as_view()),
    path('<int:pk>/delete', views.PokemonDestroyAPIView.as_view()),
    path('<int:pk>/update', views.PokemonUpdateAPIView.as_view())
]