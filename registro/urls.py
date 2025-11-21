from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"visitas", views.VisitaViewSet)



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.nuevo_registro, name="nuevo_registro"),
    path("registro/<int:id>/", views.motivo_registro, name="motivo_registro"),
    path("registro/nuevo/", views.nuevo_registro, name="nuevo_registro"),
    path("registro/editar/<int:id>/", views.editar_registro, name="editar_registro"),
    path("registro/eliminar/<int:id>/", views.eliminar_registro, name="eliminar_registro"),
    path("registro/registro_admin/", views.registro_admin, name="registro_admin"),
    path("registro/registro_visitas/", views.registro_visitas, name="registro_visitas"),
]