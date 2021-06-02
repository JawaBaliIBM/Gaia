from rest_framework import serializers

class GreetingsSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    sender = serializers.CharField(max_length=200)