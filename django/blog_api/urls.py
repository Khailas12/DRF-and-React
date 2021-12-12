from django.urls.conf import path
from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')

# urlpatterns = router.urls

urlpatterns = [
    path('', PostList.as_view({'get': 'list', 'post': 'create'}), name='listcreate'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
]