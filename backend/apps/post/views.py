from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Posts
from .serializer import PostSerializer, RegisterSerializer, LikeSerializer, CommentSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Like, Comment
from django.db.models import Q


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = super(PostView, self).get_queryset()
    #     pass


class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = Response()

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response.set_cookie(key='token', value=token.key)
        response.set_cookie(key='user', value=user.pk)
        response.set_cookie(key='username', value=serializer.validated_data['username'])
        response.status_code = status.HTTP_200_OK
        data = {
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': serializer.validated_data['username']
        }
        response.data = {"Success": "Login successfully", "data": data}
        return response


class LogoutUserView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('token')
        response.delete_cookie('user')
        response.delete_cookie('username')
        response.data = {
            'Message': "Logged Out Successfully"
        }
        return response


class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     # print(serializer.get('user'))
    #     print(serializer)
#
#         self.perform_create(serializer)
#         print(serializer.data)
#         print(serializer.data.get('user'))
#         print(serializer.data.get('post'))
#         print(serializer.data.get('value'))
#         user_id = serializer.data.get('user')
#         post_id = serializer.data.get('post')
#         all_like = Like.objects.all().count()
#         post_obj = Posts.objects.get(id=post_id)
#         print(post_obj)
#         # print(all_like)
#         filter_post_in_like = Like.objects.filter(Q(post_id=post_id) & Q(user_id=user_id)).values('value').exists()
#         print(filter_post_in_like)
#         # if filter_post_in_like:
#
#
#         # current_post = Posts.objects.get(id=post_id)
#         # if user_id in current_post.liked.all():
#
#         # print(current_post.liked.filter(id=user_id).exists())
#         # print(Like.objects.filter(user_id=user_id))
#         # if user_id in current_post.liked.all():
#
#         #     print('yes')
#         # else:
#         #     print('no')
#
#
#
#
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()




