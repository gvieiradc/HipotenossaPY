from rest_framework import generics
from pit.models import Post
from .serializers import PostSerializer


class BlogPostRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
  #  queryset = Post.objects.all()


def get_queryset(self):
    return Post.objects.all()


#def get_object(self):
 #   pk = self.kwargs.get("pk")
   # return Post.objects.get(pk=pk)