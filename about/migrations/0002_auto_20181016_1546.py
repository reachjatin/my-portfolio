# Generated by Django 2.1.2 on 2018-10-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.TextField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('phoneNo', models.IntegerField()),
                ('address', models.TextField()),
                ('languages', models.TextField()),
                ('description', models.TextField()),
                ('profilepic', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Person')),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
