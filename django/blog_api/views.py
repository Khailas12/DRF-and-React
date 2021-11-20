from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()  # post_objects = custom manager which returns the published one
    serializer_class = PostSerializer
        

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()   # filteres data and filters based on the Id <int:pk> 
    serializer_class = PostSerializer