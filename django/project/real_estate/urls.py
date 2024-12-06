from django.urls import path
from .views import (
    ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView,
    HouseListCreateView, HouseRetrieveUpdateDestroyView,
    LandListCreateView, LandRetrieveUpdateDestroyView,
    OfferListCreateView, OfferRetrieveUpdateDestroyView,
    fuzzy_search, search_within_polygon, search_clients,
    FuzzySearchView, PropertyFilterView, PropertyFuzzySearchView,
    PropertyListView, search_properties_within_polygon,
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    RealtorListCreateView, RealtorRetrieveUpdateDestroyView,
    NeedListCreateView, NeedRetrieveUpdateDestroyView, property_type_list
)

urlpatterns = [
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list-create'),
    path('apartments/<int:pk>/', ApartmentRetrieveUpdateDestroyView.as_view(), name='apartment-retrieve-update-destroy'),
    path('houses/', HouseListCreateView.as_view(), name='house-list-create'),
    path('houses/<int:pk>/', HouseRetrieveUpdateDestroyView.as_view(), name='house-retrieve-update-destroy'),
    path('lands/', LandListCreateView.as_view(), name='land-list-create'),
    path('lands/<int:pk>/', LandRetrieveUpdateDestroyView.as_view(), name='land-retrieve-update-destroy'),
    path('offers/', OfferListCreateView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', OfferRetrieveUpdateDestroyView.as_view(), name='offer-retrieve-update-destroy'),
    path('search/fuzzy/', fuzzy_search, name='fuzzy-search'),
    path('search/within_polygon/', search_within_polygon, name='search-within-polygon'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('realtors/', RealtorListCreateView.as_view(), name='realtor-list-create'),
    path('realtors/<int:pk>/', RealtorRetrieveUpdateDestroyView.as_view(), name='realtor-retrieve-update-destroy'),
    path('fuzzy_search/', FuzzySearchView.as_view(), name='fuzzy-search'),
    path('properties/filter/', PropertyFilterView.as_view(), name='property-filter'),
    path('search/fuzzy_properties/', PropertyFuzzySearchView.as_view(), name='fuzzy-search-properties'),
    path('search/within_polygon_properties/', search_properties_within_polygon, name='search-within-polygon-properties'),
    path('clients/search/', search_clients, name='search-clients'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('needs/', NeedListCreateView.as_view(), name='need-list-create'),
    path('needs/<int:pk>/', NeedRetrieveUpdateDestroyView.as_view(), name='need-retrieve-update-destroy'),
    path('property-types/', property_type_list, name='property-type-list'),
]