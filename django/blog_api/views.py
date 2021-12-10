from django.http import request
from rest_framework import generics, viewsets, filters, status
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


class PostUserWritePermission(BasePermission):
    message = 'Editing Post is Restricted, Author only'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True     # user can read-only the data
        return obj.author == request.user   # matching with the author which the user who made request
                    

# CRUD model viewset. This simplifies code comparing with the commented codes below
class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    # for the slug field access
    def get_object(self, quryset=None, *args, **kwargs):       
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, title=item)   # using letters instead of number access 
        
    def get_queryset(self):     # custom queryset
        return Post.objects.all()


"""         
# one              
class PostList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.post_objects.all()

    def list(self, request):    # accessing everything
        serializer_class = PostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)
    
    def destroy(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# two 
class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.post_objects.all()  # post_objects = custom manager which returns the published one
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()   # filteres data and filters based on the Id <int:pk> 
    serializer_class = PostSerializer

"""