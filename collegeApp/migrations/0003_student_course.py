# Generated by Django 2.2 on 2019-05-28 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeApp', '0002_auto_20190526_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='student', to='collegeApp.Course'),
        ),
    ]
