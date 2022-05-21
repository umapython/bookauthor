from .models import Book_detail,MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class Book_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book_detail
        fields='__all__'

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    def validate(self,validated_data):
        user=MyUser.objects.Filter(email=validated_data["email"])
        if not user.exists():
            raise serializers.ValidationError({"email":"email not found"})
        if not check_password(validated_data["password"],user.first().password):
            raise serializers.ValidationError({"pwd":"Incorrectpwd"})
        return validated_data

class RegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True,
                    validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password=serializers.CharField(required=True,min_length=8,write_only=True)
    contact=serializers.CharField(required=True,max_length=50)
    name=serializers.CharField(required=True,max_length=50)
    def create(self,validated_data):
        try:
            user=MyUser.objects.get(email=validated_data["email"],name=validated_data["name"])
            if user:
                user.delete()
        except MyUser.DoesNotExist:
            user=MyUser.objects.create_user(**validated_data)
            return user
