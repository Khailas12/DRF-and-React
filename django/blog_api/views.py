from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission


class PostUserWritePermission(BasePermission):  # read only data
    message = 'Editing Post is Restricted for Author only'
    
    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:  # shortcut for any of the req methods
            return True     
        
        return obj.author == request.user

class PostListView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # non authenticated users can also view data
    
    queryset = Post.post_objects.all()  # post_objects = custom manager which returns the published one
    serializer_class = PostSerializer
        


class PostDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_class = [PostUserWritePermission]
    queryset = Post.objects.all()   # filteres data and filters based on the Id <int:pk> 
    serializer_class = PostSerializer