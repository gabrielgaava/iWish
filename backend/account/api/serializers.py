from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.fields import SerializerMethodField
from account.models import User, Follower

class BasicUserSerializer(ModelSerializer):
    
    class Meta: 
        model = User
        fields = ('id', 'username')

class FollowingSerializer(ModelSerializer):

    following_user = BasicUserSerializer(many=False)

    class Meta:
        model = Follower
        fields = ('following_user', )


class UserSerializer(ModelSerializer):

    following = FollowingSerializer(many=True)
    followers = FollowingSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'email', 'phone', 'picture', 'following', 'followers', 'date_joined')


