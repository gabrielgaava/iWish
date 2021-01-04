from rest_framework.serializers import ModelSerializer
from wish.models import WishList, Wish

class WishSerializer(ModelSerializer):

    class Meta:
        model = Wish
        fields = ('id', 'id_wishlist', 'link', 'title', 'description',
         'price', 'image', 'created_at', 'updated_at')


class WishListSerializer(ModelSerializer):

    wishes = WishSerializer(many = True)

    class Meta:
        model = WishList
        fields = ('id', 'user_id', 'title', 'description', 
        'public', 'wishes', 'created_at', 'updated_at')


