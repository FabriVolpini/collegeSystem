# Generated by Django 2.2 on 2019-05-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeApp', '0005_auto_20190528_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(choices=[('Primer año', 'Primer Año'), ('Segundo año', 'Segundo Año'), ('Tercer año', 'Tercer Año'), ('Cuarto año', 'Cuarto Año'), ('Quinto año', 'Quinto Año'), ('Sexto año', 'Sexto Año'), ('Septimo año', 'Septimo Año')], default='Primer Año', max_length=50),
        ),
    ]
