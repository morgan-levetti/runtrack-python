class Personne:
    """
    Class Création Personne
    """
    personne_cree = 0
    def __init__(self):
        print("Création d'une Personne..")
        Personne.personne_cree += 1
        self.nom = input("nom : ")
        self.prenom = input("prenom : ")     

h1 = Personne()
h2 = Personne()

def sePresenter():
    print("Vous avez créé : "  + h1.nom, ' ' + h1.prenom)
    print("Vous avez créé : "  + h2.nom, ' ' + h2.prenom)
    
sePresenter()
print("Personne Actuellement crée = ")
print(Personne.personne_cree)
