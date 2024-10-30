import sqlite3

db = sqlite3.connect("gestion2.db")

# Création de tables
db.execute("create table if not exists formation(id integer, titre text)")
db.execute("create table if not exists etudiant(code integer, nom text, email text)")

# Insertion des données (tableau de formation)
db.execute("insert into formation(id, titre) values(?,?)", (1, "Python"))
db.execute("insert into formation(id, titre) values(?,?)", (2, "html"))
db.commit()

# Insertion des données (tableau des étudiants)
db.execute("insert into etudiant(code, nom, email) values(?,?,?)", (1, "youssef", "youssef@gmail.com"))
db.execute("insert into etudiant(code, nom, email) values(?,?,?)", (2, "sara", "sara@gmail.com"))
db.commit()

# Affichage du contenu des deux tables
db.row_factory = sqlite3.Row
cursor = db.execute("select * from formation")
for row in cursor:
    print(row["id"], row["titre"])

cursorb = db.execute("select * from etudiant")
for row in cursorb:
    print(row["code"], row["nom"], row["email"])

# Fonction ins(v1, v2) qui insère une nouvelle formation dans la table formation
def ins(v1, v2):
    db.execute("insert into formation(id, titre) values(?,?)", (v1, v2))
    db.commit()

# Fonction afficher(table) qui affiche le contenu de la table passée en paramètre
def afficher(table):
    cursor = db.execute(f"select * from {table}")
    for row in cursor:
        print(row["id"], row["titre"])

# Fonction modifier(v1, v2) pour modifier le titre d'une formation
def modifier(v1, v2):
    db.execute("update formation set titre = ? where id = ?", (v2, v1))
    db.commit()

# Fonction supprimer(v1) pour supprimer une formation par ID
def supprimer(v1):
    db.execute("delete from formation where id = ?", (v1,))
    db.commit()

# Tests des fonctions:
# Test de la fonction ins
print("\nInsertion d'une nouvelle formation:")
ins(3, "JavaScript")
afficher("formation")

# Test de la fonction modifier
print("\nModification du titre de la formation avec ID = 1:")
modifier(1, "Python Avancé")
afficher("formation")

# Test de la fonction supprimer
print("\nSuppression de la formation avec ID = 2:")
supprimer(2)
afficher("formation")

# Fermer la connexion à la base de données après les opérations
db.close()
