from rest_framework import serializers
from .models import Person, Country, State, City, Town


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(many=True, read_only=True)
    country = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=True, read_only=True)
    country = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Town
        fields = '__all__'
