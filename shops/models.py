from django.db import models
from django.contrib.auth.models import AbstractUser     #로그인 기본세팅 돼 있음
from .validators import validate_no_special_characters #유효값 검사

# Create your models here.

    
class Cloth(models.Model):     #옷 모델 작성
    title = models.CharField(max_length=30)
    clothes = models.CharField(max_length=20)
    price = models.IntegerField()
    RATING_CHOICE = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    rating = models.IntegerField(choices=RATING_CHOICE)
    image1 = models.ImageField(upload_to="review_pics") #업로드 경로
    image2 = models.ImageField(upload_to="review_pics", blank= True)
    image3 = models.ImageField(upload_to="review_pics", blank= True)
    content = models.TextField(default=10000)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title

class User(AbstractUser):       #settings.py에 가서 AUTH_USER_MODEL 써줘야함
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={"unique": "이미 사용중인 닉네임입니다."},     
                                  
    )
    cart = models.ManyToManyField(Cloth,related_name="cart",blank= True, db_column='title')
    

    def __str__(self) :
        return self.email