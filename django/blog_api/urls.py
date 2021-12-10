from django.urls.conf import include, path
from .views import PostList
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

router = DefaultRouter()
router.register(r'', PostList, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]