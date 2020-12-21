# Generated by Django 3.0.3 on 2020-03-21 21:03

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Stagaire', '0002_niveau'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stagaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('dateDeNaissance', models.DateTimeField()),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('mail', models.EmailField(max_length=254)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stagaire.Filiere')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stagaire.Niveau')),
            ],
        ),
    ]