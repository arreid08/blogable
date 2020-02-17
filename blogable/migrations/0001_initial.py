# Generated by Django 3.0.3 on 2020-02-17 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=50)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='blogable.Post')),
            ],
        ),
    ]
