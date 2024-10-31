import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connexion à SQLite database
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# Creation de tables pour Vehicule & Camion
cursor.execute('''CREATE TABLE IF NOT EXISTS Vehicule (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    annee_achat INTEGER,
                    prix_achat REAL,
                    prix_courant REALs
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Camion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    annee_achat INTEGER,
                    prix_achat REAL,
                    prix_courant REAL,
                    volume REAL
                )''')

class Vehicule:
    def __init__(self, annee_achat, prix_achat):
        self.annee_achat = annee_achat
        self.prix_achat = prix_achat
        self.prix_courant = 0

    def afficher(self):
        print("Véhicule acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD.")
    
    def CalculePrix(self):
        self.prix_courant = (1.0 - ((2015 - self.annee_achat) * 0.01)) * self.prix_achat

    def save_to_db(self):
        cursor.execute('INSERT INTO Vehicule (annee_achat, prix_achat, prix_courant) VALUES (?, ?, ?)', 
                       (self.annee_achat, self.prix_achat, self.prix_courant))
        conn.commit()

class Camion(Vehicule):
    def __init__(self, volume, annee_achat, prix_achat):
        super().__init__(annee_achat, prix_achat)
        self.volume = volume

    def afficher(self):
        print("Camion acheté en", self.annee_achat, "pour", self.prix_achat, "MAD, valeur actuelle", self.prix_courant, "MAD, volume", self.volume, "m3.")
    
    def CalculePrix(self):
        self.prix_courant = (1 - (0.1 * self.volume / 1000)) * self.prix_achat

    def save_to_db(self):
        cursor.execute('INSERT INTO Camion (annee_achat, prix_achat, prix_courant, volume) VALUES (?, ?, ?, ?)', 
                       (self.annee_achat, self.prix_achat, self.prix_courant, self.volume))
        conn.commit()

# GUI  
class VehicleApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Vehicle Database")
        
        #  Section Vehicule
        
        tk.Label(window, text="Ajouter un véhicule").grid(row=0, column=0, columnspan=2)
        
        tk.Label(window, text="Année d'achat").grid(row=1, column=0)
        self.year_vehicule = tk.Entry(window)
        self.year_vehicule.grid(row=1, column=1)
        
        tk.Label(window, text="Prix d'achat").grid(row=2, column=0)
        self.price_vehicule = tk.Entry(window)
        self.price_vehicule.grid(row=2, column=1)
        
        self.add_vehicule_btn = tk.Button(window, text="Ajouter un véhicule", command=self.add_vehicule)
        self.add_vehicule_btn.grid(row=3, column=0, columnspan=2)
        
        # Section Camion
        tk.Label(window, text="Ajouter un camion").grid(row=4, column=0, columnspan=2)
        
        tk.Label(window, text="Année d'achat").grid(row=5, column=0)
        self.year_camion = tk.Entry(window)
        self.year_camion.grid(row=5, column=1)
        
        tk.Label(window, text="Prix d'achat").grid(row=6, column=0)
        self.price_camion = tk.Entry(window)
        self.price_camion.grid(row=6, column=1)
        
        tk.Label(window, text="Volume").grid(row=7, column=0)
        self.volume_camion = tk.Entry(window)
        self.volume_camion.grid(row=7, column=1)
        
        self.add_camion_btn = tk.Button(window, text="Ajouter un camion", command=self.add_camion)
        self.add_camion_btn.grid(row=8, column=0, columnspan=2)
        
        # Affichage Section
        self.display_btn = tk.Button(window, text="Affichage des enregistrements", command=self.display_records)
        self.display_btn.grid(row=9, column=0, columnspan=2)
        
        self.output = tk.Text(window, height=10, width=50)
        self.output.grid(row=10, column=0, columnspan=2)
        
    def add_vehicule(self):
        year = int(self.year_vehicule.get())
        price = float(self.price_vehicule.get())
        vehicule = Vehicule(year, price)
        vehicule.CalculePrix()
        vehicule.save_to_db()
        messagebox.showinfo("Success", "Vehicule ajouté à la base.")
        
    def add_camion(self):
        year = int(self.year_camion.get())
        price = float(self.price_camion.get())
        volume = float(self.volume_camion.get())
        camion = Camion(volume, year, price)
        camion.CalculePrix()
        camion.save_to_db()
        messagebox.showinfo("Success", "Camion ajouté à la base.")
        
    def display_records(self):
        self.output.delete(1.0, tk.END)
        
        # Affichage des Vehicules
        cursor.execute('SELECT * FROM Vehicule')
        vehicles = cursor.fetchall()
        self.output.insert(tk.END, "Vehicules:\n")
        for v in vehicles:
            self.output.insert(tk.END, f"ID: {v[0]}, Année: {v[1]}, Prix d'achat: {v[2]}, Prix actuel: {v[3]}\n")
        
        # Affichage des Camions
        cursor.execute('SELECT * FROM Camion')
        camions = cursor.fetchall()
        self.output.insert(tk.END, "\nCamions:\n")
        for c in camions:
            self.output.insert(tk.END, f"ID: {c[0]}, Année: {c[1]}, Prix d'achat: {c[2]}, Prix actuel: {c[3]}, Volume: {c[4]}\n")

# Exécution de l'application
window = tk.Tk()
app = VehicleApp(window)
window.mainloop()

# Fermeture
conn.close()
