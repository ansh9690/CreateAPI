# Generated by Django 3.0.4 on 2020-08-03 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('population', models.IntegerField(default=0)),
                ('gdp', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('population', models.IntegerField(default=0)),
                ('gdp', models.FloatField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('population', models.IntegerField(default=0)),
                ('gdp', models.FloatField(default=0)),
                ('pin_code', models.CharField(max_length=25)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.State')),
            ],
        ),
    ]
