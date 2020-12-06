from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

class role(models.Model):
    role = (
        (0, '管理员'),
        (1, '教师'),
        (2,'学生')
    )
    user = models.OneToOneField(User, related_name='role', on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=role, default=0, verbose_name='角色')

    def __str__(self):
        return str(self.role)


class student(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    StuNo = models.CharField(max_length=50,verbose_name='学生学号',primary_key=True)
    StuName = models.CharField(max_length=50, verbose_name='学生姓名')
    StuSex = models.CharField(max_length=30, verbose_name='学生性别', choices=gender, default='女', null=True)
    Major = models.CharField(max_length=50, verbose_name='学生专业名称', null=True)
    CuNo = models.ForeignKey('course', on_delete=models.CASCADE, verbose_name='学生选修的课程编号', null=True) #related_name?

    def __str__(self):
        return self.StuName

    class Meta:
        ordering = ['-Major', 'StuNo']
        verbose_name = '学生'
        verbose_name_plural = '学生'


class teacher(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    TeaNo = models.CharField(max_length=50,verbose_name='教师编号',primary_key=True)
    TeaName = models.CharField(max_length=50, verbose_name='教师姓名')
    TeaSex = models.CharField(max_length=30, verbose_name='教师性别', choices=gender, default='女', null=True)
    CuNo = models.ForeignKey('course', max_length=30, on_delete=models.CASCADE, verbose_name='课程编号',null=True )
    SignNo = models.ForeignKey('sign', on_delete=models.CASCADE, verbose_name='签到编号', null=True)

    def __str__(self):
        return self.TeaName

    class Meta:
        ordering = ['-TeaName']
        verbose_name = '教师'
        verbose_name_plural = '教师'


class manager(models.Model):
    MaNo = models.CharField(max_length=50,verbose_name='管理员编号',primary_key=True)
    MaName = models.CharField(max_length=50, verbose_name='管理员姓名')


class submission(models.Model):
    SubNo = models.CharField(max_length=50, verbose_name='提交编号',primary_key=True)
    Ans = models.CharField(max_length=50, verbose_name='学生答案', null=True, blank=True)
    Score = models.FloatField(verbose_name='作业成绩')
    SubTime = models.DateTimeField(verbose_name='提交时间',default=timezone.now)
    StuNo = models.ForeignKey('student', on_delete=models.CASCADE, verbose_name='学号')
    HomeNo = models.ForeignKey('homework', on_delete=models.CASCADE, verbose_name='作业编号')

    def __str__(self):
        return self.StuNo


class course(models.Model):
    CuNo = models.CharField(max_length=50, verbose_name='课程编号',primary_key=True)
    CuName = models.CharField(max_length=50, verbose_name='课程名称')
    TeaNo = models.ForeignKey('teacher', on_delete=models.CASCADE, verbose_name='教师编号', null=True)
    HomeNo = models.ForeignKey('homework', on_delete=models.CASCADE, verbose_name='作业编号', null=True)

    def __str__(self):
        return self.CuName

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'


class sign(models.Model):
    SignNo = models.CharField(max_length=50, verbose_name='签到编号',primary_key=True)
    StuNo = models.CharField(max_length=50, verbose_name='学生学号')
    PubTime = models.DateTimeField(verbose_name='发布时间')
    SubTime = models.DateTimeField(verbose_name='签到时间', default=timezone.now)
    CuNo = models.ForeignKey('course', on_delete=models.CASCADE, verbose_name='课程编号')
    TeaNo = models.ForeignKey('teacher', on_delete=models.CASCADE, verbose_name='教师编号')

    def __str__(self):
        return self.StuNo

    class Meta:
        verbose_name = '签到'
        verbose_name_plural = '签到'


class homework(models.Model):
    HomNo = models.IntegerField(verbose_name='作业编号', primary_key=True)
    Title = models.CharField(max_length=50, verbose_name='作业标题', default='a')
    PubDate = models.DateField(verbose_name='发布日期', default=timezone.now)
    Cont = models.CharField(max_length=5000, verbose_name='作业内容')
    CorAns = models.CharField(max_length=5000, verbose_name='作业标准答案')
    TeaNo = models.ForeignKey('teacher', on_delete=models.CASCADE, verbose_name='教师编号')

    class Meta:
        ordering = ['-PubDate']

    def __str__(self):
        return self.Title
