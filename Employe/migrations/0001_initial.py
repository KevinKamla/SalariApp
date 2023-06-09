# Generated by Django 4.0.3 on 2022-04-20 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Entreprise', '0001_initial'),
        ('Indemnites', '0001_initial'),
        ('Prime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEmploye', models.CharField(max_length=50, null=True)),
                ('prenomEmploye', models.CharField(max_length=50, null=True)),
                ('dateNaissance', models.DateField(null=True)),
                ('lieuNaissance', models.CharField(max_length=50, null=True)),
                ('nationalite', models.CharField(choices=[('Allemande', 'Allemande'), ('Algérienne', 'Algérienne'), ('Angolaise', 'Angolaise'), ('Argentine', 'Argentine'), ('Américaine', 'Américaine'), ('Anglaise', 'Anglaise'), ('Australienne', 'Australienne'), ('Autrichienne', 'Autrichienne'), ('Bahamienne', 'Bahamienne'), ('Belge', 'Belge'), ('Béninoise', 'Béninoise'), ('Bisseau-Guinéene', 'Bisseau-Guinéene'), ('Brésilienne', 'Brésilienne'), ('Burkinabé', 'Burkinabé'), ('Burundi', 'Burundi'), ('Camerounaise', 'Camerounaise'), ('Canadienne', 'Canadienne'), ('cap-verdienne', 'cap-verdienne'), ('Chilienne', 'Chilienne'), ('Chinoise', 'Chinoise'), ('Colombienne', 'Colombienne'), ('Congolaise', 'Congolaise'), ('Corée du sud', 'Corée du sud'), ('Coréene', 'Coréene'), ('Cubaine', 'Cubaine'), ('Danoise', 'Danoise'), ('Egyptienne', 'Egyptienne'), ('Equatorienne', 'Equatorienne'), ('Espagnole', 'Espagnole'), ('Estonienne', 'Estonienne'), ('Etyiopienne', 'Etyiopienne'), ('Finlandaise', 'Finlandaise'), ('Française', 'Française'), ('Gabonaise', 'Gabonaise'), ('gambienne', 'gambienne'), ('ghanéene', 'ghanéene'), ('Greque', 'Greque'), ('Guinéenne', 'Guinéenne'), ('Haïtienne', 'Haïtienne'), ('Hongroise', 'Hongroise'), ('Indienne', 'Indienne'), ('Indonésienne', 'Indonésienne'), ('Irlandaise', 'Irlandaise'), ('Islandaise', 'Islandaise'), ('Israélienne', 'Israélienne'), ('Italienne', 'Italienne'), ('Ivoirienne', 'Ivoirienne'), ('Jamaïquaine', 'Jamaïquaine'), ('Japonaise', 'Japonaise'), ('Jordanienne', 'Jordanienne'), ('Kényene', 'Kényene'), ('Libye', 'Libye'), ('Marocaine', 'Marocaine'), ('Mexicaine', 'Mexicaine'), ('Motswanan', 'Motswanan'), ('Mozambique', 'Mozambique'), ('Namibie', 'Namibie'), ('Nigeria', 'Nigeria'), ('Nigérienne', 'Nigérienne'), ('Norvégienne', 'Norvégienne'), ('Pakistanaise', 'Pakistanaise'), ('Palestinienne', 'Palestinienne'), ('Péruvienne', 'Péruvienne'), ('Philippine', 'Philippine'), ('Polonaise', 'Polonaise'), ('Portugaise', 'Portugaise'), ('Québécoise', 'Québécoise'), ('Roumaine', 'Roumaine'), ('Russe', 'Russe'), ('Sénégalaise', 'Sénégalaise'), ('Suédoise', 'Suédoise'), ('Tchadienne', 'Tchadienne'), ('Tchèque', 'Tchèque'), ('Tunisienne', 'Tunisienne'), ('Vietnamienne', 'Vietnamienne'), ('Zambienne', 'Zambienne'), ('Zimbabwéenne', 'Zimbabwéenne')], max_length=50, null=True)),
                ('statusMatrimonial', models.CharField(choices=[('Marié(e)', 'Marié(e)'), ('Célibataire', 'Célibataire'), ('Divorsé(e)', 'Divorsé(e)')], max_length=50, null=True)),
                ('fonction', models.CharField(max_length=50, null=True)),
                ('typeContrat', models.CharField(choices=[('Durée déterminée', 'Durée déterminée'), ('Durée indéterminée', 'Durée indéterminée')], max_length=50, null=True)),
                ('dateRecrutement', models.DateField(null=True)),
                ('dateFin', models.DateField(null=True)),
                ('salaireBase', models.IntegerField(null=True)),
                ('salaireNet', models.IntegerField(null=True)),
                ('sexe', models.CharField(choices=[('Maxculin', 'Maxculin'), ('Féminin', 'Féminin')], max_length=10, null=True)),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Entreprise.entreprise')),
                ('indemnite', models.ManyToManyField(to='Indemnites.indemnites')),
                ('prime', models.ManyToManyField(to='Prime.prime')),
            ],
        ),
    ]
