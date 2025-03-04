from django.db import models

# Create your models here.

# ポートフォリオの Skills を管理するモデル
class MySkill(models.Model):
    skill_name = models.CharField(max_length=100, unique=True) 
    skill_learning_period = models.CharField(max_length=100)
    skill_level = models.IntegerField()
    skill_description = models.TextField()  # 学習内容の詳細を記述する
    skill_image = models.ImageField(upload_to='images/')  # 画像をアップロードする
    
    class Meta:
      db_table = 'my_skill' 

# ポートフォリオの Qualifications を管理するモデル
class MyQualification(models.Model):
    qualification_name = models.CharField(max_length=100, unique=True)
    qualification_acquisition_date = models.CharField(max_length=100) # 取得日 
    
    class Meta:
      db_table = 'my_qualification'