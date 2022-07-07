from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import include, path
from api.views import PostViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/posts/', PostViewSet)
router.register(r'api/v1/posts/{id}/', PostViewSet)
router.register(r'api/v1/groups/', GroupViewSet)
router.register(r'api/v1/groups/{id}/', GroupViewSet)
router.register(r'api/v1/posts/{id}/comments/', CommentViewSet)
router.register(r'api/v1/posts/{id}/comments/{id}/',
                CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('/api/v1/api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
