
from rest_framework.routers import DefaultRouter

from estate.views import EstateViewSet

router = DefaultRouter()

router.register(prefix='estates',basename='states',viewset=EstateViewSet)

urlpatterns = router.urls