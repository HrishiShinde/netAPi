# Generated by Django 3.2.7 on 2021-10-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_advisor_adphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='adPhoto',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
