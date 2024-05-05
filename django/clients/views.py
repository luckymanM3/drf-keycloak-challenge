from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import KeycloakAuthenticated
# from mozilla_django_oidc.contrib.drf import OIDCPermission
from rest_framework.permissions import IsAuthenticated

@permission_classes([KeycloakAuthenticated])
class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MyView(APIView):

    def get(self, request, *args, **kwargs):
       # Your code here
       return Response({"message": "Hello, world!"})