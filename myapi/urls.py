from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (
    ArtistDetailApiView,
)
router = routers.DefaultRouter()
router.register(r'artist', views.ArtistViewSet)
router.register(r'songs', views.SongsViewSet)
router.register(r'lyrc', views.LyrcViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('api/', ArtistApiView.as_view()),
    path('myapi/<int:artist_id>/', ArtistDetailApiView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]