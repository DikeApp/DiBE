# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED
from .models import User, ShareRide, HostRide
from .serializers import UserSerializer, ShareRideSerializer
from .serializers import HostRideSerializer
from django.http import Http404


def _get_object(pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareRideList(APIView):
    def get(self, request):
        shareRides = ShareRide.objects.all()
        serializer = ShareRideSerializer(shareRides, many=True)
        return Response(serializer.data)

    def post(self, request):
        shareRide = request.data
        serializer = ShareRideSerializer(data=shareRide)
        if serializer.is_valid():
            user_id = shareRide["share_ride_user_id"]
            user = _get_object(user_id)
            user.share_count += 1
            user.save(update_fields=["share_count"])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HostRideList(APIView):
    def get(self, request):
        hostRides = HostRide.objects.all()
        serializer = HostRideSerializer(hostRides, many=True)
        return Response(serializer.data)

    def post(self, request):
        hostRide = request.data
        serializer = HostRideSerializer(data=hostRide)
        if serializer.is_valid():
            user_id = hostRide["host_ride_user_id"]
            user = _get_object(user_id)
            user.host_count += 1
            user.save(update_fields=["host_count"])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get(self, request, pk, format=None):
        user = self._get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self._get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self._get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=username, password=password)
            serializer = UserSerializer(user)
        except User.DoesNotExist:
            return Response({"status": "failed"},
                            status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data, status=status.HTTP_200_OK)
