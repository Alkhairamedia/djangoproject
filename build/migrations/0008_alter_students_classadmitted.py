# Generated by Django 5.0 on 2023-12-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='classAdmitted',
            field=models.CharField(choices=[('sss1', 'sss1'), ('sss2', 'sss2'), ('sss3', 'sss3'), ('jss1', 'jss1'), ('jss2', 'jss2'), ('jss3', 'jss3')], max_length=200, null=True),
        ),
    ]