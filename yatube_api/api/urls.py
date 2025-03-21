from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = "api"

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupViewSet, basename="groups")
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("", include(router.urls)),
]
