from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.utils.text import slugify
from  datetime import datetime
from .validators import validate_file_extension






# Create your models here.
Secteur_CHOICES = (
    ('Actions Sociales', 'Actions Sociales'),
    ('Administration Gestion et Commerce', 'Administration Gestion et Commerce'),
    ('Aéronautique', 'Aéronautique'),
    ('Agroalimentaire', 'Agroalimentaire'),
    ('Arts graphiques', 'Arts graphiques'),
    ('Arts traditionnels', 'Arts traditionnels'),
    ('Audio visuel et cinéma', 'Audio visuel et cinéma'),
    ('Bâtiment et Travaux Pub1lics', 'Bâtiment et Travaux Publics'),
    ('Construction Métallique', 'Construction Métallique'),
    ('Cuir et modélisme', 'Cuir et modélisme'),
    ('Fabrication Mécanique', 'Fabrication Mécanique'),
    ('Froid et Génie Thermique', 'Froid et Génie Thermique'),
    ('Génie Électrique', 'Génie Électrique'),
    ('Industrie de l’automobile', 'Industrie de l’automobile'),
    ('Offshoring', 'Offshoring'),
    ('Plasturgie', 'Plasturgie'),
    ('Technologies de l’information', 'Technologies de l’information'),
    ('Textile et Habillement', 'Textile et Habillement'),
    ('Tourisme et Hôtellerie', 'Tourisme et Hôtellerie'),
    ('Transport et logistique', 'Transport et logistique'),
    

)

Filiere_CHOICES = (
    ('Technicien Spécialisé en Commerce TSC', 'Technicien Spécialisé en Commerce TSC'),
    ('Technicien Spécialisé en Gestion des Entreprises TSGE', 'Technicien Spécialisé en Gestion des Entreprises TSGE'),
    ('Techniques de Secrétariat de Direction TSD', 'Techniques de Secrétariat de Direction TSD'),
    ('Techniques de Développement Informatique TDI', 'Techniques de Développement Informatique TDI'),
    ('Techniques de Développement Multimédia TDM', 'Techniques de Développement Multimédia TDM'),
    ('Techniques des Réseaux Informatiques TRI', 'Techniques des Réseaux Informatiques TRI'),
    ('Technicien Spécialisé de Maintenance en Industrie Agroalimentaire', 'Technicien Spécialisé de Maintenance en Industrie Agroalimentaire'),
    ('Technicien Spécialisé en Emballage et Conditionnement', 'Technicien Spécialisé en Emballage et Conditionnement'),
    ('Technicien Spécialisé en Fabrication Industrie Agroalimentaire', 'Technicien Spécialisé en Fabrication Industrie Agroalimentaire'),
    ('Technicien Spécialisé en Hygiène et Qualité', 'Technicien Spécialisé en Hygiène et Qualité'),
    ('Technicien Spécialisé en Industrie Meunière', 'Technicien Spécialisé en Industrie Meunière'),
    ('Technicien Spécialisé Infographie', 'Technicien Spécialisé Infographie'),
    ('Technicien Spécialisé en Production Graphique', 'Technicien Spécialisé en Production Graphique'),
    ('Technicien Spécialisé en Audio visuel (Option : Image)', 'Technicien Spécialisé en Audio visuel (Option : Image)'),
    ('Technicien Spécialisé en Audio visuel (Option : Montage', 'Technicien Spécialisé en Audio visuel (Option : Montage'),
    ('Technicien Spécialisé en Audio visuel (Option : Son)', 'Technicien Spécialisé en Audio visuel (Option : Son)'),
    ('Technicien Spécialisé en Décors et Accessoires', 'Technicien Spécialisé en Décors et Accessoires'),
    ('Technicien Spécialisé en Effets Spéciaux', 'Technicien Spécialisé en Effets Spéciaux'),
    ('Technicien Spécialisé en Régie et Gestion de Production', 'Technicien Spécialisé en Régie et Gestion de Production'),
    ('Technicien Spécialisé Conducteur de Travaux : Travaux Publics', 'Technicien Spécialisé Conducteur de Travaux : Travaux Publics'),
    ('Technicien Spécialisé Géomètre Topographe', 'Technicien Spécialisé Géomètre Topographe'),
    ('Technicien Spécialisé Gros Œuvres', 'Technicien Spécialisé Gros Œuvres'),
    ('Technicien Spécialisé Patrimoine Design', 'Technicien Spécialisé Patrimoine Design'),
    ('Technicien Spécialisé Bureau d’Etude en Construction Métallique', 'Technicien Spécialisé Bureau d’Etude en Construction Métallique'),
    ('Technicien Spécialisé en Méthodes Cuir', 'Technicien Spécialisé en Méthodes Cuir'),
    ('Technicien Spécialisé de Méthodes en Fabrication Mécanique', 'Technicien Spécialisé de Méthodes en Fabrication Mécanique'),
    ('Technicien Spécialisé en Génie Climatique', 'Technicien Spécialisé en Génie Climatique'),
    ('Technicien Spécialisé en Thermique Industrielle', 'Technicien Spécialisé en Thermique Industrielle'),
    ('Technicien Spécialisé Automatisation et Instrumentation Industrielle', 'Technicien Spécialisé Automatisation et Instrumentation Industrielle'),
    ('Technicien Spécialisé des Systèmes Automatisées', 'Technicien Spécialisé des Systèmes Automatisées'),
    ('Technicien Spécialisé Maintenance des Machines Outils et Autres Machines de Production Automatisée ', 'Technicien Spécialisé Maintenance des Machines Outils et Autres Machines de Production Automatisée'),
    ('Technicien spécialisé en Diagnostic et Electronique Embarquée', 'Technicien spécialisé en Diagnostic et Electronique Embarquée'),
    ('Technico-Commercial en Vente de Véhicules et Pièces de Rechange', 'Technico-Commercial en Vente de Véhicules et Pièces de Rechange'),
    ('Technicien Spécialisé Chimie Industrielle', 'Technicien Spécialisé Chimie Industrielle'),
    ('Maintenance des Machines et Outillage en Plasturgie', 'Maintenance des Machines et Outillage en Plasturgie'),
    ('Technicien Spécialisé Transformation des Matières Composites', 'Technicien Spécialisé Transformation des Matières Composites'),
    ('Technicien Spécialisé en Contrôle Qualité Textile', 'Technicien Spécialisé en Contrôle Qualité Textile'),
    ('Techniques Habillement Industrialisation', 'Techniques Habillement Industrialisation'),
    ('Gestion Hôtelière Option : Hébergement', 'Gestion Hôtelière Option : Hébergement'),
    ('Gestion Hôtelière Option : Restauration', 'Gestion Hôtelière Option : Restauration'),
    ('Technicien Spécialisé Animateur Touristique', 'Technicien Spécialisé Animateur Touristique'),
    ('Technicien Spécialisé Agences de Voyages', 'Technicien Spécialisé Agences de Voyages'),
    
    
)
# Create your models here.
class Filiere(models.Model):
    Intitule = models.CharField(max_length = 250,choices=Filiere_CHOICES, default='Technicien Spécialisé en Commerce TSC')
    Secteur= models.CharField(max_length=250, choices=Secteur_CHOICES, default='Actions Sociales')
    

    def __str__(self):
        return self.Intitule
    
    

# everything is fine up here

Niveau_CHOICES=(
    ('Technicien spécialisé','Technicien spécialisé'),
    ('Technicien','Technicien'),
    ('Qualification','Qualification'),
    ('Spécialisation','Spécialisation'),
    ('Formation Qualifiante','Formation Qualifiante'),
    
    

)
class Niveau(models.Model):
    Intitule  = models.CharField(max_length = 150,choices=Niveau_CHOICES,default='Technicien spécialisé')



    def __str__(self):
        return self.Intitule
SEXE_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)
    
    
class Stagaire(models.Model):
    nom = models.CharField(max_length = 150, blank=True, null=True)
    prenom = models.CharField(max_length = 150,blank=True, null=True)
    Sexe = models.CharField(max_length = 250,choices=SEXE_CHOICES, default='Not defined')
    #  add sexe to stagaire field
    dateDeNaissance = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    telephone = PhoneField(blank=True)
    mail  = models.EmailField(max_length=254,blank=True, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE,blank=True, null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,blank=True, null=True)
    usern  = models.OneToOneField(User,on_delete=models.CASCADE)
    StagaireSlug = models.SlugField(max_length = 50,blank=True)
    
    
    
    

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

    def save(self, *args, **kwargs):
        self.StagaireSlug = slugify(self.prenom+self.nom)
        super(Stagaire, self).save(*args, **kwargs)

    def halfMail(self):
        x = self.mail.find("@")
        first = self.mail[0:x+1]
        return first

class Stage(models.Model):
    DateDebut = models.DateField(auto_now=False, auto_now_add=False)
    DateFin = models.DateField(auto_now=False, auto_now_add=False)
    Societe = models.CharField(max_length = 150)
    Rapport = models.FileField(blank=True, null=True,validators=[validate_file_extension])
    stagaire = models.ForeignKey(Stagaire,  on_delete=models.CASCADE)
    StageSlug = models.SlugField(max_length = 50,blank=True)
    
    
    

    def __str__(self):
        return '%s %s' % (self.stagaire.nom, self.stagaire.prenom)

    def save(self, *args, **kwargs):
        currenttime = datetime.now()
        currentaddingdate = currenttime.strftime("%m/%d/%Y, %H:%M:%S")
        self.StageSlug = slugify(self.Societe+currentaddingdate)
        super(Stage, self).save(*args, **kwargs)

    
