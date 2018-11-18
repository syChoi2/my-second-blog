from django.db import models
from django.utils import timezone


class Post(models.Model): #models은 Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
	#데이터 타입에는 텍스트, 숫자, 날짜, 사용자 같은 다른 객체 참조 등이 있습니다.
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title


class Reply(models.Model):
	ParentPost = models.ForeignKey('Post',on_delete=models.CASCADE)
	writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	input_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.text


class GuestBook(models.Model):
	writer = models.CharField(max_length=200)
	text = models.TextField()
	input_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.text


class TheqooInfoList(models.Model):
	title = models.CharField(max_length=2000)
	url = models.URLField()
	number = models.BigIntegerField()
	reply_count = models.BigIntegerField()

	def __str__(self):
		return self.text