# Generated by Django 4.1.3 on 2022-12-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrepadre', models.CharField(max_length=15)),
                ('nombremadre', models.CharField(max_length=15)),
                ('nombrehijo', models.CharField(max_length=15)),
                ('nombrehija', models.CharField(max_length=15)),
                ('dnipadre', models.IntegerField()),
                ('dnimadre', models.IntegerField()),
                ('cumplehijo', models.CharField(max_length=15)),
                ('cumplehija', models.CharField(max_length=15)),
            ],
        ),
    ]
