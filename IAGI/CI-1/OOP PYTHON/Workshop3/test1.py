import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connexion à SQLite database
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# Création de tables pour Vehicule, Camion, et Proprietaire
cursor.execute('''CREATE TABLE IF NOT EXISTS Proprietaire (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT,
                    contact TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Vehicule (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    annee_achat INTEGER,
                    prix_achat REAL,
                    prix_courant REAL,
                    proprietaire_id INTEGER,
                    FOREIGN KEY (proprietaire_id) REFERENCES Proprietaire(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Camion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    annee_achat INTEGER,
                    prix_achat REAL,
                    prix_courant REAL,
                    volume REAL,
                    proprietaire_id INTEGER,
                    FOREIGN KEY (proprietaire_id) REFERENCES Proprietaire(id)
                )''')

class Proprietaire:
    def __init__(self, nom, contact):
        self.nom = nom
        self.contact = contact

    def save_to_db(self):
        cursor.execute('INSERT INTO Proprietaire (nom, contact) VALUES (?, ?)', 
                       (self.nom, self.contact))
        conn.commit()

class Vehicule:
    def __init__(self, annee_achat, prix_achat, proprietaire_id=None):
        self.annee_achat = annee_achat
        self.prix_achat = prix_achat
        self.prix_courant = 0
        self.proprietaire_id = proprietaire_id

    def afficher(self):
        print("Véhicule acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD.")
    
    def CalculePrix(self):
        self.prix_courant = (1.0 - ((2015 - self.annee_achat) * 0.01)) * self.prix_achat

    def save_to_db(self):
        cursor.execute('INSERT INTO Vehicule (annee_achat, prix_achat, prix_courant, proprietaire_id) VALUES (?, ?, ?, ?)', 
                       (self.annee_achat, self.prix_achat, self.prix_courant, self.proprietaire_id))
        conn.commit()

class Camion(Vehicule):
    def __init__(self, volume, annee_achat, prix_achat, proprietaire_id=None):
        super().__init__(annee_achat, prix_achat, proprietaire_id)
        self.volume = volume

    def afficher(self):
        print("Camion acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD, volume", self.volume, "m3.")
    
    def CalculePrix(self):
        self.prix_courant = (1 - (0.1 * self.volume / 1000)) * self.prix_achat

    def save_to_db(self):
        cursor.execute('INSERT INTO Camion (annee_achat, prix_achat, prix_courant, volume, proprietaire_id) VALUES (?, ?, ?, ?, ?)', 
                       (self.annee_achat, self.prix_achat, self.prix_courant, self.volume, self.proprietaire_id))
        conn.commit()

# GUI  
class VehicleApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Base Véhicules")

        # Section Proprietaire 
        tk.Label(window, text="Ajouter un propriétaire").grid(row=0, column=0, columnspan=2)
        tk.Label(window, text="Nom du propriétaire").grid(row=1, column=0)
        self.proprietaire_name = tk.Entry(window)
        self.proprietaire_name.grid(row=1, column=1)

        tk.Label(window, text="Contact").grid(row=2, column=0)
        self.proprietaire_contact = tk.Entry(window)
        self.proprietaire_contact.grid(row=2, column=1)

        self.add_proprietaire_btn = tk.Button(window, text="Ajouter un propriétaire", command=self.add_proprietaire)
        self.add_proprietaire_btn.grid(row=3, column=0, columnspan=2)

        # Section Vehicule
        tk.Label(window, text="Ajouter un véhicule").grid(row=4, column=0, columnspan=2)
        tk.Label(window, text="Année d'achat").grid(row=5, column=0)
        self.year_vehicule = tk.Entry(window)
        self.year_vehicule.grid(row=5, column=1)

        tk.Label(window, text="Prix d'achat").grid(row=6, column=0)
        self.price_vehicule = tk.Entry(window)
        self.price_vehicule.grid(row=6, column=1)

        self.add_vehicule_btn = tk.Button(window, text="Ajouter un véhicule", command=self.add_vehicule)
        self.add_vehicule_btn.grid(row=7, column=0, columnspan=2)

        # Section Camion
        tk.Label(window, text="Ajouter un camion").grid(row=8, column=0, columnspan=2)
        tk.Label(window, text="Année d'achat").grid(row=9, column=0)
        self.year_camion = tk.Entry(window)
        self.year_camion.grid(row=9, column=1)

        tk.Label(window, text="Prix d'achat").grid(row=10, column=0)
        self.price_camion = tk.Entry(window)
        self.price_camion.grid(row=10, column=1)

        tk.Label(window, text="Volume").grid(row=11, column=0)
        self.volume_camion = tk.Entry(window)
        self.volume_camion.grid(row=11, column=1)

        self.add_camion_btn = tk.Button(window, text="Ajouter un camion", command=self.add_camion)
        self.add_camion_btn.grid(row=12, column=0, columnspan=2)

        # Display Section
        self.display_btn = tk.Button(window, text="Affichage des enregistrements", command=self.display_records)
        self.display_btn.grid(row=13, column=0, columnspan=2)

        self.output = tk.Text(window, height=15, width=60)
        self.output.grid(row=14, column=0, columnspan=2)

    def add_proprietaire(self):
        name = self.proprietaire_name.get()
        contact = self.proprietaire_contact.get()
        proprietaire = Proprietaire(name, contact)
        proprietaire.save_to_db()
        messagebox.showinfo("Succès", "Propriétaire ajouté à la base.")

    def add_vehicule(self):
        year = int(self.year_vehicule.get())
        price = float(self.price_vehicule.get())
        owner_name = self.proprietaire_name.get()

        cursor.execute('SELECT id FROM Proprietaire WHERE nom = ?', (owner_name,))
        result = cursor.fetchone()

        if result:
            owner_id = result[0]
            vehicule = Vehicule(year, price, owner_id)
            vehicule.CalculePrix()
            vehicule.save_to_db()
            messagebox.showinfo("Succès", "Véhicule ajouté à la base.")
        else:
            messagebox.showwarning("Erreur", "Propriétaire non trouvé.")

    def add_camion(self):
        year = int(self.year_camion.get())
        price = float(self.price_camion.get())
        volume = float(self.volume_camion.get())
        owner_name = self.proprietaire_name.get()

        cursor.execute('SELECT id FROM Proprietaire WHERE nom = ?', (owner_name,))
        result = cursor.fetchone()

        if result:
            owner_id = result[0]
            camion = Camion(volume, year, price, owner_id)
            camion.CalculePrix()
            camion.save_to_db()
            messagebox.showinfo("Succès", "Camion ajouté à la base.")
        else:
            messagebox.showwarning("Erreur", "Propriétaire non trouvé.")

    def display_records(self):
        self.output.delete(1.0, tk.END)

        # Affichage des Propriétaires
        cursor.execute('SELECT * FROM Proprietaire')
        proprietaires = cursor.fetchall()
        self.output.insert(tk.END, "Propriétaires:\n")
        for p in proprietaires:
            self.output.insert(tk.END, f"ID: {p[0]}, Nom: {p[1]}, Contact: {p[2]}\n")

        # Affichage des Vehicules
        cursor.execute('SELECT * FROM Vehicule')
        vehicles = cursor.fetchall()
        self.output.insert(tk.END, "\nVehicules:\n")
        for v in vehicles:
            self.output.insert(tk.END, f"ID: {v[0]}, Année: {v[1]}, Prix d'achat: {v[2]}, Prix actuel: {v[3]}, Propriétaire ID: {v[4]}\n")

        # Affichage des Camions
        cursor.execute('SELECT * FROM Camion')
        camions = cursor.fetchall()
        self.output.insert(tk.END, "\nCamions:\n")
        for c in camions:
            self.output.insert(tk.END, f"ID: {c[0]}, Année: {c[1]}, Prix d'achat: {c[2]}, Prix actuel: {c[3]}, Volume: {c[4]}, Propriétaire ID: {c[5]}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleApp(root)
    root.mainloop()

# Fermeture de la connexion
conn.close()
