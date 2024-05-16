from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.set_password(self.serializer_class.password)
        self.serializer_class.save()

    def perform_update(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.set_password(self.serializer_class.password)
        self.serializer_class.save()
