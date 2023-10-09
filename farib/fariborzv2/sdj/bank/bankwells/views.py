from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView 
from rest_framework.response import Response

from .searializers import BankwellSerializer
from .models import Bankwell

def index(request):
  template = loader.get_template('1.html')
  return HttpResponse(template.render())


class Bank_get(APIView):
    def get(self,request):
        bankwell = Bankwell.objects.filter(id=1)
        serializer = BankwellSerializer(bankwell, many = True)
        return Response (serializer.data)