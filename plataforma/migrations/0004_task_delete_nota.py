# Generated by Django 4.2.1 on 2023-06-13 17:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plataforma', '0003_nota_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpo', models.CharField(max_length=60)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('done', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]
