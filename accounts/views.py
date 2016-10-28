from rest_framework.viewsets import ModelViewSet
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response


class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', ]


class GetAuthToken(ObtainAuthToken):
    """
    ---
    POST:
          serializer: AuthTokenSerializer
    """

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user).key

        return Response({
            'token': token,
            'pk': user.pk,
            'role': user.role,
        })
