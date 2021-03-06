# Generated by Django 3.1.7 on 2021-03-29 09:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='username')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('primary_number', models.CharField(blank=True, max_length=20)),
                ('mobile_number_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=120)),
                ('state', models.CharField(blank=True, max_length=120)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('total_purchases', models.CharField(blank=True, max_length=20)),
                ('forgot_password_token', models.CharField(blank=True, max_length=100)),
                ('mobile_verify_token', models.CharField(blank=True, max_length=100)),
                ('email_verify_token', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('premium_seller_tag', models.BooleanField(default=False)),
                ('seller_cod', models.BooleanField(default=False)),
                ('seller_rating', models.CharField(default=0, max_length=5)),
                ('seller_margin_multiply', models.CharField(default=1.32, max_length=10)),
                ('seller_margin_addition', models.CharField(default='550', max_length=10)),
                ('is_premium', models.BooleanField(default=False, help_text='Seller is Premium or Basic', verbose_name=' Is Premium')),
                ('role', models.CharField(blank=True, choices=[('user', 'user'), ('seller', 'seller'), ('admin', 'admin')], default='user', max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('max_allowed_highlight', models.PositiveIntegerField(default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
    ]
