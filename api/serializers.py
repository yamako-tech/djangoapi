from rest_framework import serializers
from .models import Todo, Post
# Djangoデフォルトユーザ使用
from django.contrib.auth.models import User

# ユーザserializerを定義
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # デフォルトユーザとこのユーザを関連付けておく
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    # serializerでユーザ作成する場合はDjangoの`create_user`メソッドを呼び出す
    # 通常のcreateを使うとパスワードが暗号化されずに保存されてしまう
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class PostSerializer(serializers.ModelSerializer):
    # 作成日時の表示をフォーマットしておく
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created')
        
class TodoSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'created')