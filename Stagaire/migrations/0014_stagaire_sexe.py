# Generated by Django 3.0.4 on 2020-04-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stagaire', '0013_auto_20200414_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagaire',
            name='Sexe',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Not defined', max_length=250),
        ),
    ]