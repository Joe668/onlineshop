# Generated by Django 2.0.2 on 2018-03-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20180301_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='评分'),
        ),
    ]