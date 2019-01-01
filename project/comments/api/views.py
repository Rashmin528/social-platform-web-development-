from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from comments.models import Comment

from .serializers import (
	CommentSerializer,
	CommentDetailSerializer,
)

#class PostCreateAPIView(CreateAPIView):
	#queryset = Posts.objects.all()
	#serializer_class = PostCreateUpdateSerializer
	#permission_classes = [IsAuthenticated]

	#def perform_create(self, serializer):
		#serializer.save(user=self.request.user)

class CommentListAPIView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class CommentDetailAPIView(RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer
	lookup_field = 'pk'

#class PostUpdateAPIView(RetrieveUpdateAPIView):
	#queryset = Posts.objects.all()
	#serializer_class = PostCreateUpdateSerializer
	#lookup_field = 'slug'
	#permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


#class PostDeleteAPIView(DestroyAPIView):
	#queryset = Posts.objects.all()
	#serializer_class = PostDetailSerializer
	#lookup_field = 'slug'