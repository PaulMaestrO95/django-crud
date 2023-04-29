from django_filters import FilterSet, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductFilter(FilterSet):
    products = CharFilter(
        method='product_filter',
    )

    class Meta:
        model = Stock
        fields = {'products'}

    def product_filter(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(products__id=value)
        else:
            return queryset.filter(products__title__icontains=value)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
