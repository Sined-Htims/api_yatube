from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers

from .views import CommentViewSet, PostViewSet, GroupViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='get_token'),
    path('', include(router.urls))
]

#  <URLPattern '^posts/(?P<post_id>\d+)/comments/$' [name='comment-list']>,
#  <URLPattern '^posts/(?P<post_id>\d+)/comments\.(?P<format>[a-z0-9]+)/?$' [name='comment-list']>,
#  <URLPattern '^posts/(?P<post_id>\d+)/comments/(?P<pk>[^/.]+)/$' [name='comment-detail']>,
#  <URLPattern '^posts/(?P<post_id>\d+)/comments/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='comment-detail']>
