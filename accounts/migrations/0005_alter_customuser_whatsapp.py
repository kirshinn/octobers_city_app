# Generated by Django 5.2.1 on 2025-06-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=14, null=True),
        ),
    ]
