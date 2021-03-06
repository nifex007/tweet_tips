# Generated by Django 3.1.7 on 2021-03-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('tip', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('author', models.CharField(max_length=255)),
                ('likes', models.IntegerField(blank=True)),
                ('retweets', models.IntegerField(blank=True)),
                ('retweeted', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(unique=True)),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tips.tips')),
            ],
        ),
    ]
