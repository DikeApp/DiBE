from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
                required=True,
                validators=[UniqueValidator(
                            queryset=User.objects.all(),
                            message="This username is already used!"
                            )]
               )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = "__all__"
