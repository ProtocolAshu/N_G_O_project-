# Generated by Django 5.0.3 on 2024-03-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NMS_sw', '0003_rename_number_donor_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renewal',
            name='File_name',
            field=models.FileField(upload_to='performance'),
        ),
        migrations.AlterField(
            model_name='student',
            name='performance',
            field=models.FileField(upload_to='performance'),
        ),
    ]
