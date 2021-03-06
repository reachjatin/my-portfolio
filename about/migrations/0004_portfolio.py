# Generated by Django 2.1.2 on 2018-10-16 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20181016_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectpic', models.ImageField(upload_to='images/')),
                ('projecttitle', models.CharField(max_length=255)),
                ('projectsummary', models.TextField()),
                ('projectDescription', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Person')),
            ],
        ),
    ]
