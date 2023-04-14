from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Posts
from .serializer import PostSerializer, RegisterSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Like


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


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


class LikeView(APIView):
    def post(self, request):
        user = request.user
        print(user)
        post_id = request.POST.get('post_id')
        post_obj = Posts.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
        return Response(data=like, status=status.HTTP_200_OK)



