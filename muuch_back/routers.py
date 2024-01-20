from rest_framework import routers
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter as DefaultRouter
)
from django.utils.safestring import mark_safe
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_extensions.routers import ExtendedSimpleRouter as SimpleRouter

class V1RootView(routers.APIRootView):
    """
    V1 API Root
    """

    def get_view_name(self) -> str:
        return "Muuch Maaya API v1"
    
    def get_view_description(self, html=False) -> str:
        text = """
        Muuch Maaya API v1
        """
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text
        
class V1Router(DefaultRouter):
    APIRootView = V1RootView