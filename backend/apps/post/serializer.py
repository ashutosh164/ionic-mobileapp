from rest_framework import serializers
from .models import Posts, Like, Comment
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        # data = validated_data.get('user')
        print(validated_data)
        # user = self.context['request'].user
        user = validated_data.get('user')
        post = validated_data.get('post')
        print(post.id)
        print(post.author.id)
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        like, created = Like.objects.get_or_create(**validated_data)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
        return like

        # post_obj = Posts.objects.get(title=post)
        # print(post_obj.id)
        # filter_post_in_like = Like.objects.filter(Q(post_id=post.id) & Q(user_id=user.id)).values('value').exists()
        # print(filter_post_in_like)
        # print(post.liked.all())
        # if filter_post_in_like:
        #     print('yes baby')
        #     Like.objects.get(user_id=user.id).delete()

        # like, created = Like.objects.get_or_create(**validated_data)
        # if not created:
        #     if like.value == 'Like':
        #         like.value = 'Unlike'
        #     else:
        #         like.value = 'Like'
        # like.save()
        # return like


class PostSerializer(serializers.ModelSerializer):
    # like = LikeSerializer(many=True, required=False)
    # value = serializers.CharField(source='liked.value', read_only=True, required=False)

    class Meta:
        model = Posts
        fields = '__all__'
        # fields = ['id', 'title', 'desc', 'image', 'liked', 'author', 'value']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




