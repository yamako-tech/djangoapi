from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TodoViewSet, CreateUserView, TodoListView, TodoRetrieveView, PostListView, PostRetrieveView

# model viewsetsとgenericsで紐づけ方が異なる
# model viewsetsの場合はrouterで関連付ける
router = routers.DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')

# 上記以外はurlpatternsに追記
urlpatterns = [
    path('post-list', PostListView.as_view(), name='post-list'),
    path('post-detail/<str:pk>/', PostRetrieveView.as_view(), name='post-detail'),
    path('todo-list', TodoListView.as_view(), name='todo-detail'),
    path('todo-detail/<str:pk>', TodoRetrieveView.as_view(), name='todo-detail'),
    # エンドユーザ登録path
    path('register/', CreateUserView.as_view(), name='register'),
    # JWTトークンを取得するためのエンドポイント：djoserモジュールで自動的にパスを作成
    path('auth/', include('djoser.urls.jwt')),
    # 上記routerのパスを追加しておく
    path('', include(router.urls))
]
