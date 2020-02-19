# Generated by Django 3.0.3 on 2020-02-18 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogable', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blogable.Blog'),
        ),
    ]