from rest_framework import serializers

from core.models import Product, Service


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=300)
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    size = serializers.IntegerField()
    type = serializers.IntegerField()
    existence = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'id', 'existence')

    def validate_size(self, size):
        if size < 20 or size > 50:
            raise serializers.ValidationError('size range: [20, 50]')
        return size


class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    approximate_duration = serializers.DateTimeField(read_only=True)
    service_type = serializers.IntegerField()

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('created_at', 'id')

    def create(self, validated_data):
        service = Service.objects.create(**validated_data)
        return service

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

    def validate_approximate_duration(self, approximate_duration):
        if approximate_duration < 0:
            raise serializers.ValidationError('approximate_duration cannot be negative')
        return approximate_duration
