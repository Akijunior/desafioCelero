from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from desafioCelero.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', include('apps.athlete.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
