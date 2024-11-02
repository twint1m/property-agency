from django.urls import path
from .views import FuzzySearchView
from .views import (
    ApartmentListCreateView, HouseListCreateView, LandListCreateView,
    OfferListCreateView, fuzzy_search, search_within_polygon
)

urlpatterns = [
    path('search/', FuzzySearchView.as_view(), name='fuzzy_search'),
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list'),
    path('houses/', HouseListCreateView.as_view(), name='house-list'),
    path('lands/', LandListCreateView.as_view(), name='land-list'),
    path('offers/', OfferListCreateView.as_view(), name='offer-list'),
    path('search/fuzzy/', fuzzy_search, name='fuzzy-search'),
    path('search/within_polygon/', search_within_polygon, name='search-within-polygon'),

]
