import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# Create tables for Vehicule and Camion
cursor.execute('''CREATE TABLE IF NOT EXISTS Vehicule (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    annee_achat INTEGER,
                    prix_achat REAL,
                    prix_courant REAL
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

# Example usage
v1 = Vehicule(2010, 100000)
v1.CalculePrix()
v1.afficher()
v1.save_to_db()

c1 = Camion(20, 2010, 100000)
c1.CalculePrix()
c1.afficher()
c1.save_to_db()

c2 = Camion(40, 2010, 100000)
c2.CalculePrix()
c2.afficher()
c2.save_to_db()

# Retrieve data from database and display
cursor.execute('SELECT * FROM Vehicule')
vehicles = cursor.fetchall()
print("\nStored vehicles:")
for vehicle in vehicles:
    print(vehicle)

cursor.execute('SELECT * FROM Camion')
camions = cursor.fetchall()
print("\nStored camions:")
for camion in camions:
    print(camion)

# Close the connection when done
conn.close()
