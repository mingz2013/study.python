from django.http import HttpResponse

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
			<h1>Welcome to home page...</h1>
		</body>
	</html>
	'''
	return HttpResponse(htmlStr)