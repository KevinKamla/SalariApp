# Generated by Django 4.0 on 2022-05-25 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entreprise', '0003_alter_entreprise_effectif_and_more'),
        ('Adresse', '0002_remove_adresse_entreprise_adresse_valeur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adresse',
            name='entreprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Entreprise.entreprise'),
        ),
    ]