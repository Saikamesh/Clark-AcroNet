from rest_framework import serializers
from acronym.models import Acronym, Users, Suggestions

class AcronymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acronym
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = "__all__"