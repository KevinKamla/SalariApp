# Generated by Django 4.0.3 on 2022-04-21 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entreprise', '0003_alter_entreprise_effectif_and_more'),
        ('Employe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='entreprise',
        ),
        migrations.AddField(
            model_name='employe',
            name='idEntreprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employé', to='Entreprise.entreprise'),
        ),
    ]
