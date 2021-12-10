from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)


urlpatterns = [
    # jwt 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # fetching or getting token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # reftreshing token
    path('admin/', admin.site.urls),
    
    path('api/', include('blog_api.urls', namespace='blog_api')),
    
    path('api/user/', include('users.urls', namespace='users')),    # registering user
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  

    path('', include('blog.urls', namespace='blog')),
]