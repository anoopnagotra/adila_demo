# Generated by Django 3.1.7 on 2021-04-01 17:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiwazCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Goal Name')),
                ('descriptions', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Goal descriptions')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_city', to='city.city')),
            ],
            options={
                'verbose_name_plural': 'Goals',
                'db_table': 'category',
            },
        ),
    ]
