# Generated by Django 3.2.18 on 2023-04-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbooks', '0003_alter_accountbook_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbook',
            name='category',
            field=models.CharField(choices=[('01', '수입'), ('02', '지출')], max_length=20),
        ),
    ]
