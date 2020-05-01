import smtplib
import random
import uuid
from django.shortcuts import render
from rest_framework import generics, permissions, views, response, status
from django.contrib.auth import get_user_model
from user.models import AuthToken
from user.serializer import UserLoginSerializer, UserRegisterSerializer, UserPublicSerialzer
from django.core.mail import send_mail

def smtp_gmail(email, token=None):
    username = "noreply.ticketreservations@gmail.com"
    password = "Password12!"
    smtp_server = "smtp.gmail.com:587"
    email_to = email
    email_body = "The OTP for login is " + token
    email_from = "CSCI5409"

    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(username, password)
    server.sendmail(email_from, email_to, email_body)
    server.quit()

User = get_user_model()

class UserLogin(generics.GenericAPIView):
    """
    Use this end-point to authenticate a user and generate an auth token and send an OTP.

    **Url**
        ``/users/login/``

    **Permissions**
        - Any is allowed.

    **Post**
        - Validate via Serializer
        - Generate Auth Token
    """
    serializer_class = UserLoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        """
        If serializer is valid.
            - call action.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.validated_data.get('username'))
            token_obj, boolean = AuthToken.objects.get_or_create(user=user)
            # print (boolean, "NEWUSERRRRRRRRR")
            if boolean:
                token_obj.token = str(uuid.uuid4())
            token_obj.otp = str(random.randint(1000, 9999))
            token_obj.save()
            smtp_gmail(user.email, token=token_obj.otp)
            return response.Response(
                status=status.HTTP_200_OK)
        return response.Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class UserLoginFinal(generics.GenericAPIView):
    """
    Use this end-point to authenticate a user using OTP.

    **Url**
        ``/users/loginfinal/``

    **Permissions**
        - Any is allowed.

    **Post**
        - Validate via Serializer
        - Generate Auth Token
    """
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = UserPublicSerialzer
    def post(self, request):
        """
        If serializer is valid.
            - call action.
        """
        otp = request.data.get('otp', None)
        username = request.data.get('username', None)
        if otp and username:
            try:
                print (username, otp)
                token = AuthToken.objects.get(user__username=username, otp=otp)
            except Exception as e:
                print (str(e))
                token = None

            if token:
                print ('Token object found')
                token.otp=''
                token.save()
                return response.Response(
                    data=token.token,
                    status=status.HTTP_200_OK)
        return response.Response(
            status=status.HTTP_400_BAD_REQUEST)


class UserRegister(generics.GenericAPIView):
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        """
        If serializer is valid.
            - call action.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                    status=status.HTTP_200_OK)
        return response.Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)