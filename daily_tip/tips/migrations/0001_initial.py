# Generated by Django 3.1.7 on 2021-03-04 15:05

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
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tip', models.TextField()),
                ('timestamp', models.TimeField()),
                ('author', models.CharField(max_length=255)),
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
