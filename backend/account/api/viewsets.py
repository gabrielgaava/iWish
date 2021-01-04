from rest_framework.viewsets import ModelViewSet
from account.api.serializers import UserSerializer, FollowingSerializer
from account.models import User, Follower

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowingViewSet(ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowingSerializer
