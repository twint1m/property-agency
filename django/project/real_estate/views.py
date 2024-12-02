from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from Levenshtein import distance as levenshtein_distance
from .models import Client, Realtor
from .serializers import ClientSerializer, RealtorSerializer

class FuzzySearchView(generics.GenericAPIView):
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query')
        if not query:
            raise ValidationError("Search query parameter 'query' is required.")

        client_matches = self.get_fuzzy_matches(Client, query, ClientSerializer)
        realtor_matches = self.get_fuzzy_matches(Realtor, query, RealtorSerializer)

        return Response({
            "clients": client_matches,
            "realtors": realtor_matches,
        })

    def get_fuzzy_matches(self, model, query, serializer_class):
        results = []
        queryset = model.objects.all()

        for obj in queryset:
            full_name = f"{obj.first_name or ''} {obj.last_name or ''} {obj.middle_name or ''}".strip()
            if levenshtein_distance(full_name, query) <= 3:
                results.append(serializer_class(obj).data)

        return results


from rest_framework import generics
from .models import Apartment, House, Land, Offer
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer, OfferSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from shapely.geometry import Polygon, Point
from Levenshtein import distance

class ApartmentListCreateView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class LandListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

@api_view(['GET'])
def fuzzy_search(request):
    query = request.GET.get("query", "")
    results = []

    for property in Apartment.objects.all() | House.objects.all() | Land.objects.all():
        city_dist = distance(property.city or "", query)
        street_dist = distance(property.street or "", query)

        if city_dist <= 3 or street_dist <= 3:
            results.append(property)

    return Response({"results": results}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_within_polygon(request):
    polygon_coords = request.data.get("polygon")
    polygon = Polygon(polygon_coords)
    results = []

    for property in Apartment.objects.all() | House.objects.all() | Land.objects.all():
        point = Point(property.latitude, property.longitude)
        if polygon.contains(point):
            results.append(property)

    return Response({"results": results}, status=status.HTTP_200_OK)


# new
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
from rest_framework.exceptions import ValidationError

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        if not serializer.validated_data.get('phone_number') and not serializer.validated_data.get('email'):
            raise ValidationError("Either phone number or email must be provided.")
        serializer.save()

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_update(self, serializer):
        if not serializer.validated_data.get('phone_number') and not serializer.validated_data.get('email'):
            raise ValidationError("Either phone number or email must be provided.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a client associated with an offer.")
        instance.delete()