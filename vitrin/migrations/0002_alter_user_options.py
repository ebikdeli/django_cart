# Generated by Django 4.0.5 on 2022-06-20 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_go_shopping', 'user can go shopping')]},
        ),
    ]