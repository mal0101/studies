class Employe:
    def __init__(self, Identifiant, Nom, Prenom, DateNaissance, DateEmbauche, Salaire):
        self.__Identifiant = Identifiant
        self.__Nom = Nom
        self.__Prenom = Prenom
        self.__DateNaissance = DateNaissance
        self.__DateEmbauche = DateEmbauche
        self.__Salaire = Salaire
        
    def get_identifiant(self):
        return self.__Identifiant
    def get_nom(self):
        return self.__Nom
    def get_prenom(self):
        return self.__Prenom
    def get_date_naissance(self):
        return self.__DateNaissance
    def get_date_embauche(self):
        return self.__DateEmbauche
    def get_salaire(self):
        return self.__Salaire
    # Pour les méthodes Age() et Anciennete() on suppose que la date de naissance ainsi que la date d'embauche ne représente que les années dans lesquelles ces événements ont eu lieu
    def Age(self):
        return 2024 - self.__DateNaissance
    def Anciennete(self):
        return 2024 - self.__DateEmbauche
    # Méthode d'affichage
    def afficher(self):
        print("Identifiant:", self.__Identifiant)
        print("Nom:", self.__Nom)
        print("Prénom:", self.__Prenom)
        print("Date de naissance:", self.__DateNaissance)
        print("Date d'embauche:", self.__DateEmbauche)
        print("Salaire:", self.__Salaire)
        print("Age:", self.Age())
        print("Ancienneté:", self.Anciennete())
        
emp1 = Employe(10981, "Doe", "John", 1990, 2010, 2000)
emp1.afficher()
print("\n")
emp2 = Employe(257830, "Smith", "Jane", 1995, 2015, 2500)
emp2.afficher()
print("\n")
emp3 = Employe(409090, "Johnson", "Bob", 1980, 2000, 3000)
emp3.afficher()
