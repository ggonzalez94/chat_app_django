from django.shortcuts import render,redirect
from rest_framework import generics
from .serializers import MensajeslistSerializer,UserSerializer
from .models import Mensajes
from rest_framework import permissions
from django.contrib.auth.models import User                                # Django Build in User Model

class CreateView(generics.CreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Mensajes.objects.all()
    serializer_class = MensajeslistSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(sender=self.request.user)

class ListMessagesView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Mensajes.objects.all()
    serializer_class = MensajeslistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Mensajes.objects.filter(sender = user)

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

def index(request):
    if request.user.is_authenticated: #If the user is authenticated then redirect to the chat console
        return redirect('listar_mensajes/')
    if request.method == 'GET':
        return render(request, 'index.html', {})
