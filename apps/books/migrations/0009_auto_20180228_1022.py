# Generated by Django 2.0.2 on 2018-02-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180228_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorysecond',
            name='up',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='down', to='books.CategoryFirst', verbose_name='上级'),
        ),
    ]
