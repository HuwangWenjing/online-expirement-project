# Generated by Django 3.1 on 2020-12-19 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseNo', models.CharField(max_length=50, verbose_name='课程编号')),
                ('CourseName', models.CharField(max_length=50, verbose_name='课程名称')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'ordering': ['-CourseNo'],
            },
        ),
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='作业标题')),
                ('PubTime', models.DateTimeField(verbose_name='发布时间')),
                ('EndTime', models.DateTimeField(verbose_name='结束时间')),
                ('isExpired', models.BooleanField(default=False, verbose_name='是否过期')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_homework', to='job.course', verbose_name='课程编号')),
            ],
            options={
                'verbose_name': '作业',
                'verbose_name_plural': '作业',
                'ordering': ['-PubTime'],
            },
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManagerNo', models.CharField(max_length=50, verbose_name='管理员编号')),
                ('ManagerName', models.CharField(max_length=10, verbose_name='管理员姓名')),
                ('MPassword', models.CharField(max_length=50, verbose_name='管理员密码')),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='公告标题')),
                ('Content', models.CharField(max_length=5000, verbose_name='公告内容')),
                ('PubTime', models.DateTimeField(verbose_name='公告发布时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'ordering': ['-PubTime'],
            },
        ),
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='签到标题')),
                ('PubTime', models.DateTimeField(verbose_name='发布时间')),
                ('EndTime', models.DateTimeField(verbose_name='截止时间')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.course')),
            ],
            options={
                'verbose_name': '签到',
                'verbose_name_plural': '签到',
                'ordering': ['-PubTime'],
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentNo', models.CharField(max_length=50, verbose_name='学生学号')),
                ('StudentName', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('SPassword', models.CharField(max_length=50, verbose_name='学生密码')),
                ('StudentGender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=50, verbose_name='学生性别')),
                ('Course', models.ManyToManyField(related_name='course_students', to='job.course', verbose_name='课程编号')),
                ('need_to_sign', models.ManyToManyField(related_name='sign_students', to='job.sign', verbose_name='需要完成的签到')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'ordering': ['-StudentNo'],
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeacherNo', models.CharField(max_length=50, verbose_name='教师工号')),
                ('TeacherName', models.CharField(max_length=50, verbose_name='教师姓名')),
                ('TPassword', models.CharField(max_length=50, verbose_name='教师密码')),
                ('TeacherGender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=50, verbose_name='教师性别')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'ordering': ['-TeacherNo'],
            },
        ),
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, verbose_name='token')),
                ('muser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.manager')),
                ('suser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.student')),
                ('tuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentNo', models.CharField(max_length=50, verbose_name='学生学号')),
                ('SubTime', models.DateTimeField(max_length=50, verbose_name='提交时间')),
                ('TotalGrade', models.FloatField(default='0', null=True, verbose_name='总成绩')),
                ('isSubmitted', models.BooleanField(default=False, verbose_name='是否提交')),
                ('Homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.homework', verbose_name='作业编号')),
            ],
            options={
                'verbose_name': '提交',
                'verbose_name_plural': '提交',
                'ordering': ['-SubTime'],
            },
        ),
        migrations.AddField(
            model_name='sign',
            name='sign_by',
            field=models.ManyToManyField(related_name='student_signs', to='job.student', verbose_name='需要进行此次签到的学生'),
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuesNo', models.CharField(max_length=50, verbose_name='题号')),
                ('Type', models.CharField(max_length=50, verbose_name='题目类型')),
                ('Content', models.CharField(max_length=50, verbose_name='题目内容')),
                ('CorrectAnswer', models.CharField(max_length=50, verbose_name='正确答案')),
                ('Score', models.CharField(default='0', max_length=50, verbose_name='该题分值')),
                ('Homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.homework', verbose_name='作业编号')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题目',
                'ordering': ['-QuesNo'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='Student',
            field=models.ManyToManyField(related_name='student_courses', to='job.student', verbose_name='学生学号'),
        ),
        migrations.AddField(
            model_name='course',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_courses', to='job.teacher', verbose_name='教师编号'),
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuesNo', models.CharField(max_length=50, verbose_name='题目编号')),
                ('StudentAnswer', models.CharField(blank=True, max_length=50, null=True, verbose_name='学生答案')),
                ('Grade', models.FloatField(default='0', verbose_name='该题得分')),
                ('Submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='job.submission', verbose_name='提交编号')),
            ],
            options={
                'verbose_name': '学生答案',
                'verbose_name_plural': '学生答案',
                'ordering': ['-QuesNo'],
            },
        ),
        migrations.CreateModel(
            name='analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllCounts', models.IntegerField(verbose_name='需做作业人数')),
                ('SubCounts', models.IntegerField(verbose_name='已提交数量')),
                ('Average', models.FloatField(verbose_name='平均分')),
                ('Full', models.FloatField(verbose_name='满分')),
                ('Max', models.FloatField(verbose_name='最高分')),
                ('Min', models.FloatField(verbose_name='最低分')),
                ('Homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.homework', verbose_name='作业编号')),
            ],
        ),
    ]