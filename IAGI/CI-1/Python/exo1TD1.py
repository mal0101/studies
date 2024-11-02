# Exercice 1 : Gestion de Stock
# Initialisation de l'inventaire
inventaire = {
    'produits': [],
    'historique': []
}

# Fonction pour ajouter un produit
def ajouter_produit(nom, prix, quantite, categorie):
    inventaire['produits'].append({
        'nom': nom,
        'prix': prix,
        'quantite': quantite,
        'categorie': categorie,
        'ventes': 0
    })

# Fonction pour retirer un produit
def retirer_produit(nom):
    inventaire['produits'] = [produit for produit in inventaire['produits'] if produit['nom'] != nom]

# Fonction pour calculer la valeur totale du stock
def valeur_totale_stock():
    return sum(produit['prix'] * produit['quantite'] for produit in inventaire['produits'])

# Fonction pour alerter quand un produit tombe en dessous d'un seuil minimal
def alerte_seuil_minimal(seuil):
    alertes = [produit['nom'] for produit in inventaire['produits'] if produit['quantite'] < seuil]
    if alertes:
        print(f"Attention! Les produits suivants sont en dessous du seuil minimal de {seuil}: {', '.join(alertes)}")

# Fonction pour rechercher des produits par catégorie
def rechercher_par_categorie(categorie):
    return [produit for produit in inventaire['produits'] if produit['categorie'] == categorie]

# Fonction pour générer un rapport des produits les plus vendus
def rapport_produits_vendus():
    return sorted(inventaire['produits'], key=lambda x: x['ventes'], reverse=True)

# Fonction pour enregistrer une opération d'achat ou de vente
def enregistrer_operation(type_operation, nom, quantite):
    inventaire['historique'].append({
        'type': type_operation,
        'nom': nom,
        'quantite': quantite
    })
    for produit in inventaire['produits']:
        if produit['nom'] == nom:
            if type_operation == 'achat':
                produit['quantite'] += quantite
            elif type_operation == 'vente':
                produit['quantite'] -= quantite
                produit['ventes'] += quantite

# Menu principal
def menu():
    while True:
        print("\n1. Ajouter un produit")
        print("2. Retirer un produit")
        print("3. Calculer la valeur totale du stock")
        print("4. Alerter quand un produit tombe en dessous d'un seuil minimal")
        print("5. Rechercher des produits par catégorie")
        print("6. Générer un rapport des produits les plus vendus")
        print("7. Enregistrer une opération d'achat ou de vente")
        print("8. Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            nom = input("Nom du produit: ")
            prix = float(input("Prix du produit: "))
            quantite = int(input("Quantité du produit: "))
            categorie = input("Catégorie du produit: ")
            ajouter_produit(nom, prix, quantite, categorie)
        elif choix == '2':
            nom = input("Nom du produit à retirer: ")
            retirer_produit(nom)
        elif choix == '3':
            print(f"Valeur totale du stock: {valeur_totale_stock()}")
        elif choix == '4':
            seuil = int(input("Seuil minimal: "))
            alerte_seuil_minimal(seuil)
        elif choix == '5':
            categorie = input("Catégorie à rechercher: ")
            produits = rechercher_par_categorie(categorie)
            for produit in produits:
                print(produit)
        elif choix == '6':
            rapport = rapport_produits_vendus()
            for produit in rapport:
                print(produit)
        elif choix == '7':
            type_operation = input("Type d'opération (achat/vente): ")
            nom = input("Nom du produit: ")
            quantite = int(input("Quantité: "))
            enregistrer_operation(type_operation, nom, quantite)
        elif choix == '8':
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Exécution du menu
menu()


