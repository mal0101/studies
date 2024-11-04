import sqlite3

# Classe de base pour les produits
class Produit:
    def __init__(self, nom, prix, quantite, categorie):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.categorie = categorie
        self.ventes = 0

    def afficher_info(self):
        return f"Nom: {self.nom}, Prix: {self.prix}, Quantité: {self.quantite}, Catégorie: {self.categorie}"


# Classe dérivée pour les produits électroniques, ajoutant un attribut de garantie
class ProduitElectronique(Produit):
    def __init__(self, nom, prix, quantite, garantie):
        super().__init__(nom, prix, quantite, "Électronique")
        self.garantie = garantie

    def afficher_info(self):
        return super().afficher_info() + f", Garantie: {self.garantie} mois"


# Classe dérivée pour les produits alimentaires, ajoutant un attribut de date de péremption
class ProduitAlimentaire(Produit):
    def __init__(self, nom, prix, quantite, date_peremption):
        super().__init__(nom, prix, quantite, "Alimentaire")
        self.date_peremption = date_peremption

    def afficher_info(self):
        return super().afficher_info() + f", Date de péremption: {self.date_peremption}"


# Inventaire pour gérer les produits
class Inventaire:
    def __init__(self):
        self.produits = []  # Liste des produits
        # Connexion à la base de données SQLite
        self.conn = sqlite3.connect('inventaire.db')
        self.cursor = self.conn.cursor()

        # Création des tables si elles n'existent pas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prix REAL,
            quantite INTEGER,
            categorie TEXT,
            ventes INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS historique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_operation TEXT,
            nom TEXT,
            quantite INTEGER
            )
        ''')

        self.conn.commit()

    def ajouter_produit(self, produit):
        self.produits.append(produit)
        self.cursor.execute('''
            INSERT INTO produits (nom, prix, quantite, categorie, ventes)
            VALUES (?, ?, ?, ?, ?)
        ''', (produit.nom, produit.prix, produit.quantite, produit.categorie, produit.ventes))
        self.conn.commit()

    def retirer_produit(self, nom):
        self.produits = [produit for produit in self.produits if produit.nom != nom]
        self.cursor.execute('DELETE FROM produits WHERE nom = ?', (nom,))
        self.conn.commit()

    def valeur_totale_stock(self):
        return sum(produit.prix * produit.quantite for produit in self.produits)

    def alerte_seuil_minimal(self, seuil):
        alertes = [produit.nom for produit in self.produits if produit.quantite < seuil]
        if alertes:
            print(f"Attention! Les produits suivants sont en dessous du seuil minimal de {seuil}: {', '.join(alertes)}")

    def rechercher_par_categorie(self, categorie):
        return [produit for produit in self.produits if produit.categorie == categorie]

    def rapport_produits_vendus(self):
        return sorted(self.produits, key=lambda x: x.ventes, reverse=True)

    def enregistrer_operation(self, type_operation, nom, quantite):
        self.cursor.execute('''
            INSERT INTO historique (type_operation, nom, quantite)
            VALUES (?, ?, ?)
        ''', (type_operation, nom, quantite))
        self.conn.commit()

        for produit in self.produits:
            if produit.nom == nom:
                if type_operation == 'achat':
                    produit.quantite += quantite
                elif type_operation == 'vente':
                    produit.quantite -= quantite
                    produit.ventes += quantite

                self.cursor.execute('''
                    UPDATE produits
                    SET quantite = ?, ventes = ?
                    WHERE nom = ?
                ''', (produit.quantite, produit.ventes, produit.nom))
                self.conn.commit()