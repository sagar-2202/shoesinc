# Generated by Django 4.2.3 on 2023-07-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_personinfo_delete_pinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='signInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
            ],
        ),
    ]
