from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

class token(models.Model):
    muser = models.OneToOneField('Manager', on_delete=models.CASCADE)
    tuser = models.OneToOneField('Teacher', on_delete=models.CASCADE)
    suser = models.OneToOneField('Student', on_delete=models.CASCADE)
    token = models.CharField(max_length=64, verbose_name='token')

class student(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    StuNo = models.CharField(max_length=50,verbose_name='学生学号',primary_key=True)
    StuName = models.CharField(max_length=50, verbose_name='学生姓名')
    StuSex = models.CharField(max_length=30, verbose_name='学生性别', choices=gender, default='女', null=True)
    Major = models.CharField(max_length=50, verbose_name='专业名称', null=True)
    StuPassWord = models.CharField(max_length=16, verbose_name='学生密码', default='123456')

    CuNo = models.ManyToManyField(
        'course',
        related_name='students',
        verbose_name='学生选修的课程编号'
    )

    need_to_sign = models.ManyToManyField(
        'sign',
        related_name='students',
        verbose_name='需要进行此次签到的学生'
    )

    def __str__(self):
        return self.StuName

    class Meta:
        ordering = ['-Major', 'StuNo']
        verbose_name = '学生'
        verbose_name_plural = '学生'

class manager(models.Model):
    MaNo = models.CharField(max_length=50,verbose_name='管理员编号',primary_key=True)
    MaName = models.CharField(max_length=50, verbose_name='管理员姓名')
    MaPassWord = models.CharField(max_length=16, verbose_name='管理员密码', default='123456')


class notice(models.Model):
    NoticeTitle = models.CharField(max_length=60, verbose_name='通知标题', default='通知标题')
    NoticeContent = models.CharField(max_length=5000, verbose_name='通知内容', default='通知内容')
    NoticePubTime = models.DateTimeField(verbose_name='通知发布时间', default=timezone.now)

    MaNo = models.ForeignKey(
        'manager',
        on_delete=models.CASCADE,
        verbose_name='发布此通知的管理员编号'
    )


class teacher(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    TeaNo = models.CharField(max_length=50,verbose_name='教师编号',primary_key=True)
    TeaName = models.CharField(max_length=50, verbose_name='教师姓名')
    TeaSex = models.CharField(max_length=30, verbose_name='教师性别', choices=gender, default='女', null=True)
    TeaPassWord = models.CharField(max_length=16, verbose_name='教师密码', default='123456')

    def __str__(self):
        return self.TeaName

    class Meta:
        ordering = ['-TeaName']
        verbose_name = '教师'
        verbose_name_plural = '教师'


class course(models.Model):
    CuNo = models.CharField(max_length=50, verbose_name='课程编号', primary_key=True)
    CuName = models.CharField(max_length=50, verbose_name='课程名称')

    TeaNo = models.ForeignKey(
        'teacher',
        on_delete=models.CASCADE,
        verbose_name='上这门课程的教师编号'
    )

    StuNo = models.ManyToManyField(
        'student',
        related_name='courses',
        verbose_name='选修这门课程的学生学号'
    )

    def __str__(self):
        return self.CuName

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'


#和question一对多
class homework(models.Model):
    HomNo = models.IntegerField(verbose_name='作业id', primary_key=True)
    Title = models.CharField(max_length=50, verbose_name='作业标题', default='a')
    PubTime = models.DateTimeField(verbose_name='发布时间', default=timezone.now)
    SubTime = models.DateTimeField(verbose_name='提交时间', default=timezone.now)
    TotalGrade = models.FloatField(verbose_name='总成绩', default='100')
    CuNo = models.ForeignKey(
        'course',
        on_delete=models.CASCADE,
        verbose_name='课程编号'
    )

    class Meta:
        ordering = ['-PubTime']

    def __str__(self):
        return self.Title


class question(models.Model):
    QuesNo = models.IntegerField(verbose_name='题号')
    Type = models.IntegerField(verbose_name='题目类型') #1选择 2填空 3判断 4简答 5编程
    Cont = models.CharField(max_length=5000, verbose_name='题目')
    Ans = models.CharField(max_length=5000, verbose_name='答案')
    Score = models.FloatField(verbose_name='题目分值')
    Grade = models.FloatField(verbose_name='学生得分')

    isCorrect = models.BooleanField(default = False)

    HomNo = models.ForeignKey(
        'homework',
        verbose_name='作业id',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-QuesNo']

    def __str__(self):
        return self.Cont


class sign(models.Model):
    SignNo = models.CharField(max_length=50, verbose_name='签到编号', primary_key=True)
    StuNo = models.CharField(max_length=50, verbose_name='学生学号')
    PubTime = models.DateTimeField(verbose_name='发布时间')
    SubTime = models.DateTimeField(verbose_name='签到时间', default=timezone.now)

    CuNo = models.ForeignKey(
        'course',
        on_delete=models.CASCADE,
        verbose_name='课程编号'
    )

    sign_by = models.ManyToManyField(
        'student',
        related_name = 'students',
        verbose_name = '需要进行此签到的学生'
    )

    def __str__(self):
        return self.StuNo

    class Meta:
        verbose_name = '签到'
        verbose_name_plural = '签到'


# 1. pull 之前已经pull过 就不用了
# 2. commit
# 3. push 然后push 就成功了~



# class role(models.Model):
#     role = (
#         (0, '管理员'),
#         (1, '教师'),
#         (2,'学生')
#     )
#     user = models.OneToOneField(User, related_name='role', on_delete=models.CASCADE)
#     role = models.SmallIntegerField(choices=role, default=0, verbose_name='角色')

    # def __str__(self):
    #     return str(self.role)


