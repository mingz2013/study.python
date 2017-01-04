from django.shortcuts import render
from django.shortcuts import render_to_response
from Users.models import Users	# 引入Users模型
from django.http import HttpResponse	#引入HttpResponse模块
import random	#引入random模块

# Create your views here.

def home(request):
	htmlStr = '''
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
			<title>标题title</title>
			<style type="text/css">
			<!--
			body, td, th {
				font-family:华文行楷;
				font-size:24px;
			}
			-->
			</style>
		</head>
		<body>
			<h1>Welcome to Users index page...</h1>
		</body>
	</html>
	'''
	return HttpResponse(htmlStr)
	
def index(rq):
	#获取Users数据模型对应表中的数据
	latest_users_list = Users.objects.all().order_by('-username')[:5]
	return render_to_response(
	'users/index.html', 
	{
		'latest_users_list':latest_users_list
	})
	
def random_number(request):
	randNums = ''
	#进行10次循环，生成10个10以内的证书（可重复）,并累加
	for num in range(10):
		randNums = randNums + str(random.randint(num, 10-1)) + '<br/>'
	htmlStr = ''' 
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
			<title>标题title</title>
			<style type="text/css">
			<!--
			body, td, th {
				font-family:华文行楷;
				font-size:24px;
			}
			-->
			</style>
		</head>
		<body>
			<h1>Welcome to  users random number page...</h1><br/>
			生成的随机数为<br/>%s'''%randNums + '''
		</body>
	</html>
	'''
	return HttpResponse(htmlStr)
