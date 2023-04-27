from rest_framework import serializers
from .models import Posts, Like, Comment
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings

from ..account.serializers import ProfileSerializer

User = get_user_model()
from ..account.models import Profiles
from rest_framework.response import Response


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
        # user = self.context['request'].user
        user = validated_data.get('user')
        post = validated_data.get('post')
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


# class ProfileSerializer(serializers.ModelSerializer):
#     user = RegisterSerializer()
#
#     class Meta:
#         model = Profiles
#         fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='author.username', read_only=True, required=False)
    profiles_url = serializers.SerializerMethodField('get_profile_by_author_of_the_post')
    profiles_details = serializers.SerializerMethodField('get_profiles_details')
    check_user_like_post = serializers.SerializerMethodField('check_current_user_liked_post')
    total_like = serializers.SerializerMethodField('total_like_per_post')
    total_comment = serializers.SerializerMethodField('total_comment_per_post')
    current_user_profile = serializers.SerializerMethodField('get_current_user_profiles_details')

    def get_profile_by_author_of_the_post(self, instance):
        profile = Profiles.objects.filter(user_id=instance.author.id).values_list('image', flat=True)
        request = self.context.get('request')
        # print(*profile)
        # print(profile[0])
        image_path = request.build_absolute_uri(settings.MEDIA_URL + profile[0])
        return image_path

    def get_profiles_details(self, instance):
        response = Profiles.objects.filter(user_id=instance.author.id).values()
        # print(response)
        return response

    def get_current_user_profiles_details(self, instance):
        user_id = self.context['request'].user.id
        # print(user_id)
        profile_obj = Profiles.objects.filter(user_id=user_id)
        profile = profile_obj.values()
        # print(profile)
        request = self.context.get('request')
        profile_image = profile_obj.values_list('image', flat=True)
        image_url = request.build_absolute_uri(settings.MEDIA_URL + profile_image[0])
        # print(image_url)

        return profile, image_url

    def check_current_user_liked_post(self, instance):
        liked_data = list(instance.liked.values_list(flat=True))
        # print(liked_data)
        user_id = self.context['request'].user.id
        result = filter(lambda x: x == user_id, liked_data)
        return result

    def total_like_per_post(self, instance):
        total = instance.liked.all().count()
        return total

    def total_comment_per_post(self, instance):
        total = instance.comments.all().count()
        return total

    class Meta:
        model = Posts
        fields = '__all__'
        # fields = ['id', 'title', 'desc', 'image', 'liked', 'author', 'user_name', 'profiles']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




