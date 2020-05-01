from django.contrib.auth import get_user_model
from rest_framework import serializers
from booking.models import Booking

User = get_user_model()

class BookingSerializer(serializers.Serializer):
    """
    Serializer Booking

    **Validate**
        - validate user exists with given username
        - Use UserService to verify credentials.

    **Create**
        - None
    """
    username = serializers.CharField()
    number_of_passengers = serializers.CharField()
    bus_route = serializers.CharField()
    destination = serializers.CharField()
    amount_paid = serializers.CharField()

    def validate(self, data):
        username = data.get('username').lower()
        try:
            user = User.objects.get(username=username)
        except:
            raise serializers.ValidationError(
                "Validation Error: User doesn't exist")
        data['user'] = user
        return data

    def create(self, validated_data):
        booking = Booking(
            user=validated_data.get('user'),
            number_of_passengers=validated_data.get('number_of_passengers'),
            bus_route=validated_data.get('bus_route'),
            destination=validated_data.get('destination'),
            amount_paid=validated_data.get('amount_paid'))
        booking.save()
        return booking
    class Meta:
        model = Booking
        fields = '__all__'


class BookingPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'number_of_passengers', 'bus_route', 'destination', 'amount_paid', 'user']
