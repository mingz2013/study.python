from django.db import models

# Create your models here.
#创建一个User数据模型
class Users(models.Model):
	username = models.CharField('用户名', max_length = 20)	#生成字段
	password = models.CharField('密码', max_length = 20)
	realname = models.CharField('真实姓名', max_length = 255)
	sex = models.CharField('性别', max_length = 10)
	email = models.EmailField('电子邮箱', blank = True)
	
	def __str__(self):
		 return '%s'%(self.name)