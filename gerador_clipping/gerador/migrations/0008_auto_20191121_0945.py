# Generated by Django 2.2.7 on 2019-11-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerador', '0007_remove_news_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='news',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
