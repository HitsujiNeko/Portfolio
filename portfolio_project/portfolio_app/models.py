from django.db import models

# Create your models here.

# Profileを管理するモデル
class Profile(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    about_me = models.TextField()
    profile_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

# Skills を管理するモデル
class MySkill(models.Model):
    skill_name = models.CharField(max_length=100, unique=True) 
    skill_learning_period = models.CharField(max_length=100)
    skill_level = models.IntegerField()
    skill_description = models.TextField()  # 学習内容の詳細を記述する
    skill_image = models.ImageField(upload_to='images/')  # 画像をアップロードする
    
    class Meta:
      db_table = 'my_skill' 

# Qualifications を管理するモデル
class MyQualification(models.Model):
    qualification_name = models.CharField(max_length=100, unique=True)
    qualification_acquisition_date = models.CharField(max_length=100) # 取得日 
    
    class Meta:
      db_table = 'my_qualification'
    
# Apps を管理するモデル
from django.db import models

class App(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title