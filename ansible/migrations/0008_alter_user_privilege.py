# Generated by Django 4.0.1 on 2022-01-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0007_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privilege',
            field=models.ManyToManyField(blank=True, null=True, to='ansible.Host'),
        ),
    ]
