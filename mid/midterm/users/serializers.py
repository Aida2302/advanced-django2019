from django.db import transaction
from rest_framework import serializers
from users.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'address')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()
    # is_super_admin = serializers.BooleanField(default=False)
    # is_store_admin = serializers.BooleanField(default=False)
    # is_guest = serializers.BooleanField(default=True)
    # role = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile')

    def create(self, validated_data):
        with transaction.atomic():
            profile_data = validated_data.pop('profile')
            user = User.objects.create_user(**validated_data)
            Profile.objects.create(user=user, **profile_data)
            return user

