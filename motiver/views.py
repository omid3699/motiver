import random
from rest_framework.views import APIView
from rest_framework.response import Response
from config.data import DATA


# Create your views here.


class RandomQuoteView(APIView):
    def get(self, request):
        return Response(random.choice(DATA))
