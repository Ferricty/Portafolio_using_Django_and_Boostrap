# Generated by Django 4.0.5 on 2022-07-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
    ]
