from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .serializers import UserSerializer, TestSerializer


# Create your views here.
class GetUser(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        view to return current user
        """
        user_ = self.request.user.username
        return self.queryset.filter(username=user_)


class TestView(generics.ListAPIView):
    """
    Test view to illustrate permissions
    """

    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = TestSerializer
    queryset = User.objects.all()
