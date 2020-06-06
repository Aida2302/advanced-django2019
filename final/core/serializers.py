from rest_framework import serializers

from core.models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ('owner',)

    def create(self, validated_data):
        account = Account.objects.create(**validated_data)
        return account

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

    def validate_min_amount(self, value):
        if value < 1000:
            raise serializers.ValidationError('min amount to withdraw money is 1000')
        return value

    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError('you are out of money')
        return value


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('account',)

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        return transaction
