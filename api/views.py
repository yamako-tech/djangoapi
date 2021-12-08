from rest_framework.permissions import AllowAny
from rest_framework import generics 
from rest_framework import viewsets
from .serializers import TodoSerializer, UserSerializer, PostSerializer
from .models import Todo, Post
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # 初回のユーザ作成時は誰でもアクセス出来るようにしておく
    permission_classes = (AllowAny,)
    
# ブログ投稿データ取得のエンドポイント設定
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 投稿・編集・削除以外のパーミッションはAllowAnyにしておく
    permission_classes = (AllowAny,)
    
# idと紐づいた投稿詳細画面   
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    
class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permisson_classes = (AllowAny,)
    
class TodoRetrieveView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (AllowAny,)

# TodoのCRUD設定
# ModelViewSetはデフォルトでCRUDが全て使える
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # パーミッションを上書きせず、デフォルトのJWTトークンを適用させる