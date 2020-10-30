from rest_framework import routers

from apps.athlete.views import AthleteViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'atletas', AthleteViewSet, basename='athlete')
router.register(r'criar-usuario', UserViewSet, basename='create_user')