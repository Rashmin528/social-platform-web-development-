from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
)

from posts.models import Posts

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = [
        	'user',
            'title',
            'slug',
            'content',
		]

class PostListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='detailapi',
		lookup_field='slug'
		)
	user = SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
			'url',
			'user',
        	'id',
        	'user',
            'title',
            'slug',
            'content',
            'image',
		]
	def get_user(self, obj):
		return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
        	'user',
        	'id',
        	'user',
            'title',
            'slug',
            'content',
            'image',
		]
	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image
