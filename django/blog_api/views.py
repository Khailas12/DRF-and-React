from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    message = 'Editing Post is Restricted, Author only'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True     # user can read-only the data
        return obj.author == request.user   # matching with the author which the user who made request
                    

class PostListView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.post_objects.all()  # post_objects = custom manager which returns the published one
    serializer_class = PostSerializer
        

class PostDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()   # filteres data and filters based on the Id <int:pk> 
    serializer_class = PostSerializer