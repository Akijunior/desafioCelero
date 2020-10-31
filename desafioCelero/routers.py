from rest_framework import routers

from apps.athlete.views import AthleteViewSet, UserViewSet, GameViewSet,\
    SportViewSet, EventViewSet

router = routers.DefaultRouter()

router.register(r'atletas', AthleteViewSet, basename='athlete')
router.register(r'esportes', SportViewSet, basename='sport')
router.register(r'eventos', EventViewSet, basename='event')
router.register(r'jogos', GameViewSet, basename='game')
router.register(r'criar-usuario', UserViewSet, basename='create_user')