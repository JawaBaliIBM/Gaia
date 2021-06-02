from rest_framework import viewsets
from rest_framework.response import Response
import sys
sys.path.append("..")

from quickstart.serializer import GreetingsSerializer

class GreetingsViewSet(viewsets.ViewSet):
    serializer_class = GreetingsSerializer

    def list(self, request):
        payload = [{'message': 'welcome to gaia project', 'sender': 'fellita'}]
        serializer = GreetingsSerializer(
            instance=payload, many=True)
        return Response(serializer.data)
