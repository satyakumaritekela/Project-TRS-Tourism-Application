from django.shortcuts import render
from rest_framework import generics, permissions, views, response, status
from django.contrib.auth import get_user_model
from booking.models import Booking
from booking.serializer import BookingSerializer, BookingPublicSerializer
from user.models import AuthToken

User = get_user_model()

class CreateBooking(generics.GenericAPIView):
    serializer_class = BookingSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                    status=status.HTTP_200_OK)
        return response.Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class ListBooking(generics.ListAPIView):
    model = Booking
    serializer_class = BookingPublicSerializer
    def get_queryset(self):
        token = self.request.query_params.get('token').strip("\"")
        # print (token)
        queryset = []
        try:
            user = AuthToken.objects.get(token=token).user
            # print (user)
        except Exception as e:
            # print (str(e))
            return queryset
        if user:
            queryset = self.model.objects.filter(user=user)
            # print (queryset)
            return queryset