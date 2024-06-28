from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework import status,viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


# http://127.0.0.1:8000/accounts/register
class UserRegisterView(APIView):

    def post(self,request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()

    def list(self,request):
        srz_data = UserSerializer(instance=self.queryset,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        srz_data = UserSerializer(instance=user)
        return Response(srz_data.data,status=status.HTTP_200_OK)

    def create(self,request):
        pass

    def update(self,request,pk=None):
        pass

    def partial_update(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user != request.user:
            return Response({'message':'You are not the owner of this account.'})
        srz_data = UserSerializer(instance=user,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user != request.user:
            return Response({'message':'You are not the owner of this account.'})
        user.is_active = False
        user.save()
        return Response({'message':'The desired user was deactivated'})

