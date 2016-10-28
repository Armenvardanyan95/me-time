# -*- coding: utf-8 -*-

from rest_framework import serializers

from .utils import is_invalid_password


def check_valid_password(data):
    invalid_password_message = is_invalid_password(data.get('password'), data.get('repeat_password'))
    if invalid_password_message:
        raise serializers.ValidationError({'password': invalid_password_message})