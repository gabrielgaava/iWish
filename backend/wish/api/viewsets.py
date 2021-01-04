from rest_framework.viewsets import ModelViewSet
from wish.api.serializers import WishListSerializer, WishSerializer
from wish.models import WishList, Wish


class WishViewSet(ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

class WishListViewSet(ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer