# Generated by Django 5.0 on 2023-12-23 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_rename_firstname_staffs_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('studentId', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('classAdmitted', models.CharField(max_length=200, null=True)),
                ('currentClass', models.CharField(choices=[('sss1', 'sss1'), ('sss2', 'sss2'), ('sss3', 'sss3'), ('jss1', 'jss1'), ('jss2', 'jss2'), ('jss3', 'jss3')], max_length=200, null=True)),
                ('dateAdmitted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('book', models.CharField(max_length=200, null=True)),
                ('deptCategory', models.CharField(choices=[('science', 'science'), ('commercial', 'commercial'), ('art', 'art')], max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='staffs',
            old_name='classIncharge',
            new_name='description',
        ),
        migrations.AddField(
            model_name='staffs',
            name='category',
            field=models.CharField(choices=[('classteacher', 'classteacher'), ('subject_teacher', 'subject_teacher'), ('helper', 'helper'), ('cleaner', 'cleaner'), ('driver', 'driver'), ('security', 'security')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('classAdmitted', models.CharField(max_length=200, null=True)),
                ('childAdmitedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInjSS1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInjSS2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInjSS3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInSSS1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInSSS2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
        migrations.CreateModel(
            name='studentsInSSS3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='build.students')),
            ],
        ),
    ]
