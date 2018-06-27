from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'products-api'

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
