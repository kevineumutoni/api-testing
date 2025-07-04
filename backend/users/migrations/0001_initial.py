# Generated by Django 5.2.3 on 2025-07-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('password_hash', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('vendor', 'Vendor (Mama Mboga)'), ('customer', 'Customer (Buyer)')], max_length=20)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('till_number', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
