from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDestroyAPIView(generics.DestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonUpdateAPIView(generics.UpdateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer