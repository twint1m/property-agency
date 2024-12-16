from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from Levenshtein import distance as levenshtein_distance
from .models import Client, Realtor, Property, Deal
from .serializers import ClientSerializer, RealtorSerializer, DealSerializer




from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from fuzzywuzzy import fuzz
from .models import Client, Realtor
from .serializers import ClientSerializer, RealtorSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from fuzzywuzzy import fuzz
from .models import Client, Realtor
from .serializers import ClientSerializer, RealtorSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from fuzzywuzzy import fuzz
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
            ratio = fuzz.partial_ratio(full_name.lower(), query.lower())
            if ratio >= 70:  # Adjust the threshold as needed
                results.append(serializer_class(obj).data)

        return results


from rest_framework import generics
from .models import Apartment, House, Land, Offer
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer, OfferSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from shapely.geometry import Point
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



from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from Levenshtein import distance as levenshtein_distance
from .models import Client, Realtor
from .serializers import ClientSerializer, RealtorSerializer

class RealtorListCreateView(generics.ListCreateAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

    def perform_create(self, serializer):
        if not serializer.validated_data.get('first_name') or not serializer.validated_data.get('last_name') or not serializer.validated_data.get('middle_name'):
            raise ValidationError("First name, last name, and middle name are required.")
        serializer.save()

class RealtorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

    def perform_update(self, serializer):
        if not serializer.validated_data.get('first_name') or not serializer.validated_data.get('last_name') or not serializer.validated_data.get('middle_name'):
            raise ValidationError("First name, last name, and middle name are required.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a realtor associated with an offer.")
        instance.delete()


from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

class ApartmentListCreateView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class LandListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

class ApartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a property associated with an offer.")
        instance.delete()

class HouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a property associated with an offer.")
        instance.delete()

class LandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a property associated with an offer.")
        instance.delete()


from django.db.models import Q
from .serializers import PropertySerializer

# django/project/real_estate/views.py
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.db.models import Value, CharField
from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

class PropertyFilterView(generics.ListAPIView):
    def get_serializer_class(self):
        first_object = self.get_queryset().first()
        if isinstance(first_object, Apartment):
            return ApartmentSerializer
        elif isinstance(first_object, House):
            return HouseSerializer
        elif isinstance(first_object, Land):
            return LandSerializer
        raise ValidationError("No valid property type found.")

    def get_queryset(self):
        property_type = self.request.query_params.get('type')
        city = self.request.query_params.get('city')
        street = self.request.query_params.get('street')

        common_fields = ['id', 'city', 'street', 'house_number', 'apartment_number', 'latitude', 'longitude', 'area']
        apartment_fields = common_fields + ['floor', 'rooms']
        house_fields = common_fields + ['floors', 'rooms']
        land_fields = common_fields

        queryset = Apartment.objects.none()
        if property_type:
            if property_type.lower() == 'apartment':
                queryset = Apartment.objects.values(*apartment_fields).annotate(property_type=Value('apartment', output_field=CharField()))
            elif property_type.lower() == 'house':
                queryset = House.objects.values(*house_fields).annotate(property_type=Value('house', output_field=CharField()))
            elif property_type.lower() == 'land':
                queryset = Land.objects.values(*land_fields).annotate(property_type=Value('land', output_field=CharField()))
        else:
            apartment_queryset = Apartment.objects.values(*apartment_fields).annotate(property_type=Value('apartment', output_field=CharField()))
            house_queryset = House.objects.values(*house_fields).annotate(property_type=Value('house', output_field=CharField()))
            land_queryset = Land.objects.values(*land_fields).annotate(property_type=Value('land', output_field=CharField()))
            queryset = apartment_queryset.union(house_queryset, land_queryset)

        if city:
            queryset = queryset.filter(city__icontains=city)
        if street:
            queryset = queryset.filter(street__icontains=street)

        return queryset

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shapely.geometry import Point
from Levenshtein import distance as levenshtein_distance
from .models import Apartment, House, Land

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shapely.geometry import Point
from Levenshtein import distance as levenshtein_distance
from .models import Apartment, House, Land

@api_view(['GET'])
def fuzzy_search_properties(request):
    query_city = request.GET.get("city", "")
    query_street = request.GET.get("street", "")
    query_house_number = request.GET.get("house_number", "")
    query_apartment_number = request.GET.get("apartment_number", "")
    results = []

    apartments = Apartment.objects.all()
    houses = House.objects.all()
    lands = Land.objects.all()

    for property in apartments:
        city_dist = levenshtein_distance(property.city or "", query_city)
        street_dist = levenshtein_distance(property.street or "", query_street)
        house_number_dist = levenshtein_distance(property.house_number or "", query_house_number)
        apartment_number_dist = levenshtein_distance(property.apartment_number or "", query_apartment_number)

        if city_dist <= 3 and street_dist <= 3 and house_number_dist <= 1 and apartment_number_dist <= 1:
            results.append({
                "type": "Apartment",
                "id": property.id,
                "city": property.city,
                "street": property.street,
                "house_number": property.house_number,
                "apartment_number": property.apartment_number
            })

    for property in houses:
        city_dist = levenshtein_distance(property.city or "", query_city)
        street_dist = levenshtein_distance(property.street or "", query_street)
        house_number_dist = levenshtein_distance(property.house_number or "", query_house_number)
        apartment_number_dist = levenshtein_distance(property.apartment_number or "", query_apartment_number)

        if city_dist <= 3 and street_dist <= 3 and house_number_dist <= 1 and apartment_number_dist <= 1:
            results.append({
                "type": "House",
                "id": property.id,
                "city": property.city,
                "street": property.street,
                "house_number": property.house_number,
                "apartment_number": property.apartment_number
            })

    for property in lands:
        city_dist = levenshtein_distance(property.city or "", query_city)
        street_dist = levenshtein_distance(property.street or "", query_street)
        house_number_dist = levenshtein_distance(property.house_number or "", query_house_number)
        apartment_number_dist = levenshtein_distance(property.apartment_number or "", query_apartment_number)

        if city_dist <= 3 and street_dist <= 3 and house_number_dist <= 1 and apartment_number_dist <= 1:
            results.append({
                "type": "Land",
                "id": property.id,
                "city": property.city,
                "street": property.street,
                "house_number": property.house_number,
                "apartment_number": property.apartment_number
            })

    return Response({"results": results}, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

@api_view(['POST'])
def search_properties_within_polygon(request):
    try:
        polygon_coords = request.data.get('polygon', [])
        # Преобразуйте координаты в полигон без использования GDAL или Shapely
        # Например, можно использовать простую проверку координат

        apartments = Apartment.objects.filter(latitude__isnull=False, longitude__isnull=False)
        houses = House.objects.filter(latitude__isnull=False, longitude__isnull=False)
        lands = Land.objects.filter(latitude__isnull=False, longitude__isnull=False)

        apartment_serializer = ApartmentSerializer(apartments, many=True)
        house_serializer = HouseSerializer(houses, many=True)
        land_serializer = LandSerializer(lands, many=True)

        results = apartment_serializer.data + house_serializer.data + land_serializer.data

        return Response({"results": results}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from Levenshtein import distance as levenshtein_distance

@api_view(['GET'])
def search_clients(request):
    query = request.GET.get("query", "")
    results = []

    for client in Client.objects.all():
        full_name = f"{client.first_name or ''} {client.last_name or ''}".strip()
        if levenshtein_distance(full_name.lower(), query.lower()) <= 3:
            results.append(client)

    serializer = ClientSerializer(results, many=True)
    return Response({"clients": serializer.data}, status=status.HTTP_200_OK)



    from rest_framework import generics
    from rest_framework.response import Response
    from rest_framework.exceptions import ValidationError
    from Levenshtein import distance as levenshtein_distance
    from .models import Apartment, House, Land
    from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from Levenshtein import distance as levenshtein_distance
from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

class PropertyFuzzySearchView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query_city = request.query_params.get('city', '')
        query_street = request.query_params.get('street', '')
        query_house_number = request.query_params.get('house_number', '')
        query_apartment_number = request.query_params.get('apartment_number', '')

        if not query_city and not query_street and not query_house_number and not query_apartment_number:
            raise ValidationError("At least one search parameter is required.")

        apartments = Apartment.objects.all()
        houses = House.objects.all()
        lands = Land.objects.all()

        apartment_matches = self.get_fuzzy_matches(Apartment, query_city, query_street, query_house_number, query_apartment_number, ApartmentSerializer)
        house_matches = self.get_fuzzy_matches(House, query_city, query_street, query_house_number, query_apartment_number, HouseSerializer)
        land_matches = self.get_fuzzy_matches(Land, query_city, query_street, query_house_number, query_apartment_number, LandSerializer)

        print(f"Search query: city={query_city}, street={query_street}, house_number={query_house_number}, apartment_number={query_apartment_number}")
        print(f"Apartment matches: {apartment_matches}")
        print(f"House matches: {house_matches}")
        print(f"Land matches: {land_matches}")

        return Response({
            "results": {
                "apartments": apartment_matches,
                "houses": house_matches,
                "lands": land_matches,
            }
        })

    def get_fuzzy_matches(self, model, query_city, query_street, query_house_number, query_apartment_number, serializer_class):
        results = []
        queryset = model.objects.all()

        for obj in queryset:
            city_dist = levenshtein_distance(obj.city or "", query_city) if query_city else 0
            street_dist = levenshtein_distance(obj.street or "", query_street) if query_street else 0
            house_number_dist = levenshtein_distance(obj.house_number or "", query_house_number) if query_house_number else 0
            apartment_number_dist = levenshtein_distance(obj.apartment_number or "", query_apartment_number) if query_apartment_number else 0

            print(f"Comparing: {obj.city} with {query_city}, distance: {city_dist}")
            print(f"Comparing: {obj.street} with {query_street}, distance: {street_dist}")
            print(f"Comparing: {obj.house_number} with {query_house_number}, distance: {house_number_dist}")
            print(f"Comparing: {obj.apartment_number} with {query_apartment_number}, distance: {apartment_number_dist}")

            if (not query_city or city_dist <= 3) and (not query_street or street_dist <= 3) and (not query_house_number or house_number_dist <= 1) and (not query_apartment_number or apartment_number_dist <= 1):
                results.append(serializer_class(obj).data)

        return results

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Apartment, House, Land
from .serializers import ApartmentSerializer, HouseSerializer, LandSerializer

class PropertyListView(APIView):
    def get(self, request, *args, **kwargs):
        apartments = Apartment.objects.all()
        houses = House.objects.all()
        lands = Land.objects.all()

        apartment_serializer = ApartmentSerializer(apartments, many=True)
        house_serializer = HouseSerializer(houses, many=True)
        land_serializer = LandSerializer(lands, many=True)

        results = [
            {"type": "apartment", **data} for data in apartment_serializer.data
        ] + [
            {"type": "house", **data} for data in house_serializer.data
        ] + [
            {"type": "land", **data} for data in land_serializer.data
        ]

        return Response(results)


from rest_framework import generics
from .models import Offer
from .serializers import OfferSerializer

class OfferRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

from rest_framework import generics
from .models import Need
from .serializers import NeedSerializer
from rest_framework.exceptions import ValidationError

class NeedListCreateView(generics.ListCreateAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

class NeedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

    def perform_destroy(self, instance):
        if instance.offers.exists():
            raise ValidationError("Cannot delete a need associated with an offer.")
        instance.delete()

from rest_framework import generics
from .models import Need
from .serializers import NeedSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class NeedListCreateView(generics.ListCreateAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

class NeedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

@api_view(['GET'])
def property_type_list(request):
    property_types = [{"value": choice[0], "label": choice[1]} for choice in Need.PROPERTY_TYPE_CHOICES]
    return Response(property_types)

# django/project/real_estate/views.py

# django/project/real_estate/views.py

from rest_framework import generics
from .models import Deal
from .serializers import DealSerializer
from rest_framework.exceptions import ValidationError

# django/project/real_estate/views.py
from rest_framework import generics
from .models import Deal
from .serializers import DealSerializer
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

class DealListCreateView(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def perform_create(self, serializer):
        need = serializer.validated_data.get('need')
        offer = serializer.validated_data.get('offer')
        if hasattr(need, 'deal') or hasattr(offer, 'deal'):
            raise ValidationError("The selected need or offer is already part of another deal.")
        try:
            serializer.save()
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise ValidationError("An unexpected error occurred.")

class DealRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def perform_update(self, serializer):
        need = serializer.validated_data['need']
        offer = serializer.validated_data['offer']
        if hasattr(need, 'deal') or hasattr(offer, 'deal'):
            raise ValidationError("The selected need or offer is already part of another deal.")
        serializer.save()


from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from django.utils.timezone import now

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        today = now().date()
        return Event.objects.filter(datetime__date=today)

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer