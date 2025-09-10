# from model_apps.core.mixins.staffrequired import StaffRequiredMixin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


class ProtectedSpectacularAPIView(
    # StaffRequiredMixin,
    SpectacularAPIView,
):
    pass


class ProtectedSwaggerView(
    # StaffRequiredMixin,
    SpectacularSwaggerView,
):
    pass


class ProtectedRedocView(
    # StaffRequiredMixin,
    SpectacularRedocView,
):
    pass
