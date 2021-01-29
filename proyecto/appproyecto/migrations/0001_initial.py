# Generated by Django 3.1.5 on 2021-01-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motocicleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('velocidad', models.CharField(max_length=4)),
                ('cambio', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=50)),
            ],
        ),
    ]
