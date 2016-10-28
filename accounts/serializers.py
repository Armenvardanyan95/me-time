from rest_framework import serializers
from accounts.models import User
from core.utils import generate_unique_key
from .validators import check_valid_password


class UserSerializer(serializers.HyperlinkedModelSerializer):

    repeat_password = serializers.CharField(required=False, write_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="api:users-detail")

    class Meta:
        model = User
        exclude_password = ('password', 'repeat_password',)
        exclude_other_fields = ('is_superuser', 'is_staff', 'groups', 'user_permissions',)
        exclude = exclude_other_fields
        read_only_fields = ('token', 'last_login', 'created', 'modified', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        validated_data.pop('repeat_password', None)
        new_object = super(UserSerializer, self).create(validated_data)
        new_object.token = generate_unique_key(new_object.email)
        new_object.save()
        return new_object

    def validate(self, data):
        data['username'] = data['email']
        check_valid_password(data)
        if data.get('email'):
            self.__check_unique_email(data)

        return data

    def __check_unique_email(self, data):

        exist = User.objects.filter(email=data['email'])
        if self.instance:
            exist = exist.exclude(pk=self.instance.pk)

        if exist.exists():
            raise serializers.ValidationError({'email': 'This email is already taken.'})