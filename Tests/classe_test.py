# Permet de vider le terminal du texte inutile
import os
os.system('cls')

# pour importer d'autre fonction: from ... (math, random..., ou un de mes fichiers avec des fonction qui se trouve dans le meme dossier)
#                                 import * (* = toutes les fonctions)

class Voiture():
    def __init__(self):
        self.vitesse = 0 # Attribut

    def accelerer(self, v:int): # Méthode (comme une fonction)
        '''
        Permet d'augmenter la vitesse de la voiture de v km/h

        Paramètres:
            v (int) : L'augmentation de la vitesse
        '''
        self.vitesse += v

    def freiner(self, v):
        self.vitesse -= v

    def get_vitesse(self):
        return self.vitesse

ma_voiture = Voiture()
ma_voiture.accelerer(10)
ma_voiture.freiner(2)
print(ma_voiture.get_vitesse())