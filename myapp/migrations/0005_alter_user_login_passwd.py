# Generated by Django 4.0 on 2025-01-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_data_set_question_pool_type_master_user_exam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='passwd',
            field=models.CharField(max_length=128),
        ),
    ]
