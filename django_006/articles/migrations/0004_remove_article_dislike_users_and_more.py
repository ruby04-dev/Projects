# Generated by Django 4.2 on 2023-04-17 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_article_dislike_users_comment_dislike_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='dislike_users',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislike_users',
        ),
        migrations.AddField(
            model_name='article',
            name='emote_users',
            field=models.ManyToManyField(related_name='emote_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Emote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=10)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
