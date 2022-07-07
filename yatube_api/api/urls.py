from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import include, path
from .views import PostViewSet, CommentViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/posts/', PostViewSet)
router.register(r'api/v1/posts/{post_id}/', PostViewSet)
router.register(r'api/v1/groups/', GroupViewSet)
router.register(r'api/v1/groups/{group_id}/', GroupViewSet)
router.register(r'api/v1/posts/{post_id}/comments/', CommentViewSet)
router.register(r'api/v1/posts/{post_id}/comments/{comment_id}/',
                CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
