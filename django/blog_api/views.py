from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication,BasicAuthentication
from rest_framework import filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


class PostUserWritePermission(BasePermission):
    message = 'Editing Post is Restricted, Author only'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True     # user can read-only the data
        return obj.author == request.user   # matching with the author which the user who made request
                    

# CRUD model viewset. This simplifies code comparing with the commented codes below
@action(detail=False, methods=['GET'])
class PostList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    
    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        queryset = Post.objects.all()
        
        if author:
            return queryset.filter(user=author)

        return queryset
    
"""
class PostList(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,TokenAuthentication)
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user.id
        return Post.objects.filter(author=user) # makes user posts to their belonging
"""

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [PostUserWritePermission]
    # queryset = Post.objects.all()   # filteres data and filters based on the Id <int:pk> 
    serializer_class = PostSerializer

    def get_queryset(self):
       slug = self.request.query_params.get('slug', None)
       return Post.objects.filter(slug=slug)
    
class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]    # ?search=
    search_fields = ['^slug']
    
    """ Basic functions
    1. '^' Starts-with search
    2. '=' Exact matches
    3. '@' Full-text search (Currently only supported Django's PostgreSQL backend)
    4. '$' Regex search
    """
    
class PostSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']
   
"""                    
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

class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.post_objects.all()  # post_objects = custom manager which returns the published one
    serializer_class = PostSerializer
"""
