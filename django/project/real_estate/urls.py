from django.urls import path
from .views import (
    ApartmentListCreateView, HouseListCreateView, LandListCreateView,
    OfferListCreateView, fuzzy_search, search_within_polygon,
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    RealtorListCreateView, RealtorRetrieveUpdateDestroyView,
    FuzzySearchView
)

urlpatterns = [
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list'),
    path('houses/', HouseListCreateView.as_view(), name='house-list'),
    path('lands/', LandListCreateView.as_view(), name='land-list'),
    path('offers/', OfferListCreateView.as_view(), name='offer-list'),
    path('search/fuzzy/', fuzzy_search, name='fuzzy-search'),
    path('search/within_polygon/', search_within_polygon, name='search-within-polygon'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('realtors/', RealtorListCreateView.as_view(), name='realtor-list-create'),
    path('realtors/<int:pk>/', RealtorRetrieveUpdateDestroyView.as_view(), name='realtor-retrieve-update-destroy'),
    path('fuzzy_search/', FuzzySearchView.as_view(), name='fuzzy-search'),
]