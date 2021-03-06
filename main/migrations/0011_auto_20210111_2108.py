# Generated by Django 3.1.5 on 2021-01-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_students_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course',
            field=models.IntegerField(default=2, verbose_name='Курс'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('y', 'Учится'), ('n', 'Отчсилен'), ('q', 'Зачислен'), ('a', 'Решается')], max_length=1),
        ),
    ]
