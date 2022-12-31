from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return current user
        """
        user_ = self.request.user.username
        return self.queryset.filter(username=user_)
    


    
