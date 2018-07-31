from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	# アップロード用
	url(r'upload/', views.form, name='form'),
	# file
	path('file/', views.file_root, name='file_root'),
	# file以下
	path('file/<param>/', views.file_child,  name='file_child'),
	# パラメータが来たとき
	path('<param>/', views.index_param,  name='index_param'),
	# パラメータなし
	path('', views.index, name='index'),
] 
