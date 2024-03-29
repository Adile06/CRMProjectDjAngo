# Generated by Django 3.1.4 on 2024-03-11 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_agent_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='leads.agent'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lead',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
