# Generated by Django 5.0.1 on 2024-03-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nutri', '0004_alter_food_food_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.IntegerField(default=0),
        ),
    ]
