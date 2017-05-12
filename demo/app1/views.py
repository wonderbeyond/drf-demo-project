from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CompanySerializer
from .models import Company
from .filters import CompanyFilter


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_class = CompanyFilter

    filter_backends = [DjangoFilterBackend]
