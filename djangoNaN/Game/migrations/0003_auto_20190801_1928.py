# Generated by Django 2.2.3 on 2019-08-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_paris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paris',
            name='equipe',
            field=models.CharField(max_length=50),
        ),
    ]
