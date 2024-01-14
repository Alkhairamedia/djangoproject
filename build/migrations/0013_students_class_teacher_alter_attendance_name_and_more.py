# Generated by Django 5.0 on 2024-01-13 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0012_parents_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.teachers'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='parents',
            name='child',
            field=models.ManyToManyField(to='build.students'),
        ),
    ]
