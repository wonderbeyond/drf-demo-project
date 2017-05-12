from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from app1.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'app1/companies', CompanyViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
