
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer User login

    **Validate**
        - validate user exists with given username
        - Use UserService to verify credentials.

    **Create**
        - None
    """

    username = serializers.CharField()

    password = serializers.CharField(
        style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username').lower()
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            raise serializers.ValidationError(
                "Validation Error: User doesn't exist")
        if not user.check_password(password):
            raise serializers.ValidationError(
                "Validation Error: User doesn't exist")
        # print (data, "SERIALZER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return data

    class Meta:
        fields = ('username', 'password')

class UserRegisterSerializer(serializers.Serializer):
    """
    Serializer User login

    **Validate**
        - None

    **Create**
        - User
    """
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,)

    def validate(self, data):
        try:
            user = User.objects.get(username=data.get('username'))
        except Exception as e:
            user = None
        if user:
            raise serializers.ValidationError(
                "User already exists")

        return data

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class UserPublicSerialzer(serializers.Serializer):
    username = serializers.CharField()
    otp = serializers.CharField()
    class Meta:
        model = User
        fields = ('username', 'otp')