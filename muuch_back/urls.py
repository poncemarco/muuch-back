from django.contrib import admin
from django.urls import path, include
from .routers import V1Router
from items.views import ItemViewSet, CategoryViewSet
from orders.views import OrderViewSet
from django.conf.urls.static import static
from django.conf import settings
from .views import test_view


routerv1 = V1Router()
routerv1.trailing_slash = "/?"
routerv1.register(r'items', ItemViewSet)
routerv1.register(r'orders', OrderViewSet)
routerv1.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(routerv1.urls)),
    path('test/', test_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
