from rest_framework.generics import ListAPIView

from myshop.models import User
from myshop.serializers import UserCreateCustomSerializer


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer