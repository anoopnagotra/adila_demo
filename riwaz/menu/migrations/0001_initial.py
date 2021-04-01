# Generated by Django 3.1.7 on 2021-04-01 17:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiwazMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_menu', to='category.riwazcategory')),
            ],
            options={
                'verbose_name_plural': 'Department',
                'db_table': 'menu',
            },
        ),
    ]