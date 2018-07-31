# HttpResponseの生成用
from django.shortcuts import render
from django.http.response import HttpResponse

# shareディレクトリ内にあるファイルの中身を見る用
from pathlib import Path
import os

# アップロードし終わったときにもとのページに飛ばす用
from django.http import HttpResponseRedirect

# 現在時刻取得用
import datetime

# shareディレクトリ内
def file_root(request):
	file_list = [] # ファイル名保存用

	# Pathオブジェクトを生成
	p = Path("./static/share/")

	# ファイルのパスとファイル名をリストにして保存
	for i in list(p.glob("*")):
		file_list.append(check_ext(i))


	# パラメータを渡す
	response = {'param1': file_list}

	return render(request, 'index_param.html', response)

# shareディレクトリ以下
def file_child(request, param):
	return render(request, 'index.html')
	file_list = [] # ファイル名保存用

	# Pathオブジェクトを生成
	p = Path("./static/share/")

	# ファイルのパスとファイル名をリストにして保存
	for i in list(p.glob("*")):
		file_list.append(check_ext(i))


	# パラメータを渡す
	response = {'param1': file_list}

	return render(request, 'index_param.html', response)

# パラメータあり
def index_param(request, param):
	return render(request, 'index.html')

# ホームページ
def index(request):
	return render(request, 'index.html')



# アップロードの受け皿
def form(request):
	# GETで来たら/file/に飛ばす
	if request.method != 'POST':
        	return HttpResponseRedirect('/file/')
    
	# ファイルアップロード（複数）
	# ファイルのリストをとる
	# htmlでname="upfile"で指定
	files = request.FILES.getlist('upfile[]')

	# 現在時刻取得
	now = datetime.datetime.now()

	# 一つづつファイル操作
	for i in range(len(files)):
        	# パスの指定
        	path1 = os.path.join("static/share/", (str(now) + " " + str(files[i])))
        	# ファイルを保存
        	with open(path1, 'wb') as ff:
         		ff.write(files[i].file.read())
	
	# アップロードが終わったら/file/に戻る
	return HttpResponseRedirect('/file/')



# 拡張子のチェック
def check_ext(path):
	file_basename = os.path.basename(path)
	_, file_extention = os.path.splitext(file_basename)

	# text
	extention_list = [".txt"]
	class_name = "fa-file-alt"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# image
	extention_list = [".gif", ".jpg", ".jpeg", ".jpe", ".png", ".bmp", ".ico", ".ai", ".psd"]
	class_name = "fa-file-image"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# audio
	extention_list = [".mp3", ".wav"]
	class_name = "fa-file-audio"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# movie
	extention_list = [".mov", ".mpg", ".mpeg", ".wma"]
	class_name = "fa-file-video"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# archive
	extention_list = [".zip", ".tar.gz", ".tar", ".tgz", ".gz", ".lzh"]
	class_name = "fa-file-archive"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# pdf
	extention_list = [".pdf"]
	class_name = "fa-file-pdf"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# word
	extention_list = [".doc", ".docm", ".docx", ".dot", ".dotx"]
	class_name = "fa-file-word"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# excel
	extention_list = [".xls", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xlw"]
	class_name = "fa-file-excel"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]
	# powerpoint
	extention_list = [".ppt", ".pps", ".pptx", ".pptm"]
	class_name = "fa-file-powerpoint"
	for i in extention_list:
		if file_extention == i:
			return [class_name, path, file_basename]

	# other extention
	class_name = "fa-file"
	return [class_name, path, file_basename]



