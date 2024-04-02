from rest_framework import serializers
from .models import promotiontable

class promotion_serilizer(serializers.ModelSerializer):
    class Meta:
        model = promotiontable
        fields = "__all__"

class hr_serilizer(serializers.ModelSerializer):
    class Meta:
        model = promotiontable
        fields = ["id","elgibility"]
        # fields = "__all__"