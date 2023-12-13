from rest_framework import generics, authentication, permissions, status
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import User


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ModifyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Obtén el usuario por su ID
        user_id = self.kwargs.get('pk')
        return User.objects.get(id=user_id)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MiembrosListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer