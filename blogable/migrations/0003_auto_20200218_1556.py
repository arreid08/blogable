# Generated by Django 3.0.3 on 2020-02-18 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogable', '0002_post_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog',
            new_name='blog_content',
        ),
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blogable.Post'),
        ),
    ]