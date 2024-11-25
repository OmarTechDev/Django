from rest_framework.routers import DefaultRouter

from Booking.views import BookingViewSet

router = DefaultRouter()

router.register(prefix='',basename='bookings',viewset=BookingViewSet)

urlpatterns = router.urls