from rest_framework import serializers
from django.contrib.auth.models import User
from awareness.models import Post,Answer
from usermanagement.models import UserProfile
from socialdistancing.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','title','description'] 


class AnswerSerialier(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','user','upvote','downvote','post','reply']               


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifiaction
        fields = '__all__'