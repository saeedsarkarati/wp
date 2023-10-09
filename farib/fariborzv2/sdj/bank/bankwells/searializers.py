from rest_framework import serializers

from .models import Bankwell

class BankwellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankwell
        fields = '__all__'