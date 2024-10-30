class Personne:
    def __init__(self, nom,adresse):
        self.nom = nom
        self.adresse = adresse
        
    def afficher(self):
        print("Nom: ", self.nom)
        print("Adresse: ", self.adresse)
        
class employe(Personne):
    def __init__(self, cnss, nom, adresse):
        self.cnss = cnss
        Personne.__init__(self, nom, adresse)    
    def afficher(self):
        print("CNSS:", self.cnss)
        Personne.afficher(self)
        
class enseignant(Personne):
    def __init__(self, cnops, nom, adresse):
        self.cnops = cnops
        Personne.__init__(self, nom, adresse)    
    def afficher(self):
        print("CNOPS:", self.cnops)
        Personne.afficher(self)
                
class etudiant(Personne):
    def __init__(self, cne, nom, adresse):
        self.cne = cne
        Personne.__init__(self, nom, adresse)   
    def afficher(self):
        print("CNE:", self.cne)
        Personne.afficher(self)
        
e1 = employe(2323, 'omary', 'blablabla')
e1.afficher()
        
