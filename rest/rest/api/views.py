# rest/api/views.py
from rest_framework.generics import ListCreateAPIView

from ..models import Posts
from .serializers import PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer