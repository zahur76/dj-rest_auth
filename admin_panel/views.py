from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
class GetUser(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsAdminUser, IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        view to return current user
        """
        user_ = self.request.user.username
        print(user_)
        return self.queryset.filter(username=user_)


class TestView(generics.ListAPIView):

    serializer_class = [NotImplemented]

    def get_queryset(self):
        return Response(status=200)

