from django.urls import converters
from django.urls.converters import IntConverter


class username_converter(IntConverter):
    regex = '[a-zA-Z0-9_-]{5,20}'
    def to_pyton(self,value):
        return value
