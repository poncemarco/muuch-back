from django.contrib import admin
from django.urls import path, include
from .routers import V1Router
from items.views import ItemViewSet
from orders.views import OrderViewSet


routerv1 = V1Router()
routerv1.trailing_slash = "/?"
routerv1.register(r'items', ItemViewSet)
routerv1.register(r'orders', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(routerv1.urls)),
]
