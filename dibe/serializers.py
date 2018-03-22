from rest_framework import serializers
from .models import User, ShareRide, HostRide
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    # username = serializers.CharField(
    #             min_length=8,
    #             validators=[UniqueValidator(
    #                         queryset=User.objects.all(),
    #                         message="This username is already used!"
    #                         )]
    #            )
    # password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = "__all__"


class ShareRideSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareRide
        fields = "__all__"


class HostRideSerializer(serializers.ModelSerializer):

    class Meta:
        model = HostRide
        fields = "__all__"
