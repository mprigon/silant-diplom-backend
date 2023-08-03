from rest_framework import serializers
from .models import *


class LoaderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    modelOfLoader = serializers.StringRelatedField(many=False)
    modelOfEngine = serializers.StringRelatedField(many=False)
    modelOfTransmission = serializers.StringRelatedField(many=False)
    modelOfLeadingAxle = serializers.StringRelatedField(many=False)
    modelOfSteerAxle = serializers.StringRelatedField(many=False)
    client = serializers.StringRelatedField(many=False)
    serviceCompanyLoader = serializers.StringRelatedField(many=False)

    class Meta:
        model = Loader
        fields = "__all__"


class TechServiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    loaderOnTechService = serializers.StringRelatedField(many=False)
    techServiceCompany = serializers.StringRelatedField(many=False)

    class Meta:
        model = TechService
        fields = "__all__"


class ClaimsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    loaderOnClaim = serializers.StringRelatedField(many=False)
    repairServiceCompany = serializers.StringRelatedField(many=False)
    durationDownTime=serializers.StringRelatedField(many=False)

    class Meta:
        model = Claims
        fields = "__all__"


class ModelLoaderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ModelLoader
        fields = "__all__"
        