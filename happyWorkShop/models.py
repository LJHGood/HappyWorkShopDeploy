from django.db import models

# Create your models here.


class ContactUsModel(models.Model):
    name = models.CharField(max_length=20, verbose_name="이름")
    email = models.CharField(max_length=50, verbose_name="이메일")
    phone = models.CharField(max_length=20, verbose_name="전화번호")
    content = models.CharField(max_length=100, verbose_name="문의내용")

    def __str__(self):
        return str(self.id) + " " + self.name + "   " + self.phone + "   " + self.email + "   " + self.content

    class Meta:
        verbose_name = '문의내용'


class IntroduceModel(models.Model):
    content = models.TextField(max_length=200, verbose_name="소개글")
    youtubeLink = models.CharField(max_length=200, verbose_name="유튜브링크")

    def __str__(self):
        return str(self.id) + " " + self.content

    class Meta:
        verbose_name = '소개 페이지'


class RepresentativeIntroductionModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="대표자이름")
    profileImage = models.ImageField(upload_to="images", verbose_name="썸네일 사진")
    contentImage = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="본문 사진")

    current_history = models.TextField(max_length=10000, null=True, blank=True, verbose_name="현재 이력")
    past_history = models.TextField(max_length=10000, null=True, blank=True, verbose_name="과거 이력")
    qualification = models.TextField(max_length=10000, null=True, blank=True, verbose_name="자격 내용")

    content = models.TextField(max_length=10000, null=True, blank=True, verbose_name="내용")

    def getCurrentHistory(self):
        return self.current_history.splitlines()

    def getPastHistory(self):
        return self.past_history.splitlines()

    def getcontent(self):
        return self.content.splitlines()
        

    def __str__(self):
        return str(self.id) + " " + self.name

    class Meta:
        verbose_name = '대표소개 페이지'

class ServiceModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="서비스 이름")
    profileImage = models.ImageField(upload_to="images", verbose_name="서비스 사진")
    content = models.TextField(max_length=10000, verbose_name="서비스 내용")

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.content

    class Meta:
        verbose_name = '서비스 페이지'


class ReviewModel(models.Model):
    image = models.ImageField(blank=True, upload_to="images", null=True, verbose_name="후기 사진")
    name = models.CharField(max_length=200, verbose_name="후기 이름")
    title = models.CharField(max_length=500, verbose_name="후기 제목")
    content = models.TextField(max_length=10000, verbose_name="후기 내용")

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.title + " " + self.content

    class Meta:
        verbose_name = '후기 페이지'


class QuestionModel(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.id) #+ " " + self.image

    class Meta:
        verbose_name = '상담받기 페이지'

class FooterModel(models.Model):
    logo = models.ImageField(upload_to="images", verbose_name="로고 이미지")
    title = models.CharField(max_length=10, verbose_name="제목")
    content = models.TextField(max_length=100, verbose_name="내용")

    def __str__(self):
        return str(self.id) #+ " " + self.image

    class Meta:
        verbose_name = '바닥 페이지'
