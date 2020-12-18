from django.db import models


class token(models.Model):
    muser = models.OneToOneField('manager', on_delete=models.CASCADE, null=True)
    tuser = models.OneToOneField('teacher', on_delete=models.CASCADE, null=True)
    suser = models.OneToOneField('student', on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=64, verbose_name='token')


class manager(models.Model):
    ManagerNo=models.CharField(verbose_name='管理员编号', max_length=50)
    ManagerName=models.CharField(verbose_name='管理员姓名', max_length=10)
    MPassword=models.CharField(verbose_name='管理员密码', max_length=50)

    def __str__(self):
        return self.ManagerName


class teacher(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    TeacherNo=models.CharField(verbose_name='教师编号', max_length=50)
    TeacherName=models.CharField(verbose_name='教师姓名', max_length=50)
    TPassword=models.CharField(verbose_name='教师密码', max_length=50)

    class Meta:
        ordering = ['-TeacherNo']
        verbose_name = '教师'
        verbose_name_plural = verbose_name


class student(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    StudentNo = models.CharField(verbose_name='学生学号', max_length=50)
    SPassword = models.CharField(verbose_name='学生密码', max_length=50)

    CourseNo = models.ManyToManyField(
        'course',
        verbose_name='课程编号',
        related_name='course_students'
    )


class course(models.Model):
    CourseNo=models.CharField(verbose_name='课程编号', max_length=50, null=True)

    TeacherNo=models.ForeignKey(
        'teacher',
        verbose_name='教师编号',
        on_delete=models.CASCADE,
    )

    StudentNo=models.ManyToManyField(
        'student',
        verbose_name='学生学号',
        related_name='student_courses',
    )


class homework(models.Model):
    # HomeworkID=models.CharField(verbose_name='作业编号')
    Title=models.CharField(verbose_name='作业标题', max_length=50)
    PubTime=models.DateTimeField(verbose_name='发布时间')
    EndTime=models.DateTimeField(verbose_name='结束时间')

    isExpired=models.BooleanField(verbose_name='是否过期', default=False)

    CourseNo=models.ForeignKey(
        'course',
        verbose_name='课程编号',
        on_delete=models.CASCADE,
    )


class question(models.Model):
    QuesNo=models.CharField(verbose_name='题号', max_length=50)
    Type=models.CharField(verbose_name='题目类型', max_length=50)
    Content=models.CharField(verbose_name='题目内容', max_length=50)
    CorrectAnswer=models.CharField(verbose_name='正确答案', max_length=50)
    Score=models.CharField(verbose_name='该题分值', max_length=50, default='0')

    HomeworkID=models.ForeignKey(
        'homework',
        verbose_name='作业编号',
        on_delete=models.CASCADE,
    )


class submission(models.Model):
    SubmissionID=models.CharField(verbose_name='提交编号', max_length=50)
    StudentNo=models.CharField(verbose_name='学生学号', max_length=50)
    SubTime=models.CharField(verbose_name='提交时间', max_length=50)
    TotalGrade=models.FloatField(verbose_name='总成绩', default='0')

    isSubmitted=models.BooleanField(verbose_name='是否提交', default=False)

    HomeworkID=models.ForeignKey(
        'homework',
        verbose_name='作业编号',
        on_delete=models.CASCADE,
    )


class answer(models.Model):
    QuesNo=models.CharField(verbose_name='题目编号', max_length=50)
    StudentAnswer=models.CharField(verbose_name='学生答案', max_length=50)
    Grade=models.FloatField(verbose_name='该题得分', default='0')

    SubmissionID=models.ForeignKey(
        'submission',
        verbose_name='提交编号',
        on_delete = models.CASCADE,
    )


class analysis(models.Model):
    AllCounts=models.IntegerField(verbose_name='需做作业人数')
    SubCounts=models.IntegerField(verbose_name='已提交数量')
    Average=models.CharField(verbose_name='平均分', max_length=50)
    Full=models.CharField(verbose_name='满分', max_length=50)
    Max=models.CharField(verbose_name='最高分', max_length=50)
    Min=models.CharField(verbose_name='最低分', max_length=50)
    # 每个分数的分布人数
    # 每道题的正确率

    HomeworkID=models.ForeignKey(
        'homework',
        verbose_name='作业编号',
        on_delete=models.CASCADE,
    )


