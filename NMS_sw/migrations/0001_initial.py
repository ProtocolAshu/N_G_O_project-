# Generated by Django 5.0.3 on 2024-03-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Donor',
            },
        ),
        migrations.CreateModel(
            name='Donor_avail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Donor_avail',
            },
        ),
        migrations.CreateModel(
            name='Renewal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.FileField(upload_to='performance_cards/')),
            ],
            options={
                'db_table': 'Renewal',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('class_field', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
                ('performance_card', models.FileField(upload_to='performance_cards/')),
                ('guardian_name', models.CharField(max_length=100)),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
