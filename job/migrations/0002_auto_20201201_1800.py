# Generated by Django 2.1.15 on 2020-12-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='Ans',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='学生答案'),
        ),
    ]