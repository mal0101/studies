class Vehicule:
    def __init__(self, annee_achat, prix_achat):
        self.annee_achat = annee_achat
        self.prix_achat = prix_achat
    def afficher(self):
        print("Véhicule acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD.")
    def CalculePrix(self):
        self.prix_courant = (1.0 - ((2015 - self.annee_achat) * 0.01) * self.prix_achat)

class Camion(Vehicule):
    def __init__(self, volume, annee_achat, prix_achat):
        Vehicule.__init__(self, annee_achat, prix_achat)
        self.volume = volume
    def afficher(self):
        print("Camion acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD, volume", self.volume, "m3.")
    def CalculePrix(self):
        self.prix_courant = (1 -( 0.1 * self.volume / 1000 ) ) * self.prix_achat
    
    
v1 = Vehicule(2010, 100000)
v1.CalculePrix()
v1.afficher()
c1 = Camion(20, 2010, 100000)
c2 = Camion(40, 2010, 100000)
c1.CalculePrix()
c2.CalculePrix()
c1.afficher()
c2.afficher()

