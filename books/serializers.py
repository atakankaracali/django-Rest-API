from rest_framework import serializers
from .models import Book


class BookSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "description"]
