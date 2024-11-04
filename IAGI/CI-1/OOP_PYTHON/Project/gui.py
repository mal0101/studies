import tkinter as tk
from tkinter import messagebox
from inventaire_classes import Inventaire, ProduitElectronique, ProduitAlimentaire

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de l'Inventaire")
        self.inventaire = Inventaire()
        self.type_produit = tk.StringVar()

        self.create_type_selection_page()

    def create_type_selection_page(self):
        print("Creating type selection page")
        self.clear_frame()

        self.frame_type = tk.Frame(self.root)
        self.frame_type.pack(pady=10)

        tk.Label(self.frame_type, text="Choisissez le type de produit:").pack()

        self.electronique_btn = tk.Radiobutton(self.frame_type, text="Électronique", variable=self.type_produit, value="electronique")
        self.electronique_btn.pack()

        self.alimentaire_btn = tk.Radiobutton(self.frame_type, text="Alimentaire", variable=self.type_produit, value="alimentaire")
        self.alimentaire_btn.pack()

        self.suivant_btn = tk.Button(self.frame_type, text="Suivant", command=self.create_product_info_page)
        self.suivant_btn.pack(pady=10)

    def create_product_info_page(self):
        print("Creating product info page")
        self.clear_frame()

        self.frame_ajout = tk.Frame(self.root)
        self.frame_ajout.pack(pady=10)

        tk.Label(self.frame_ajout, text="Nom:").grid(row=0, column=0)
        self.nom_entry = tk.Entry(self.frame_ajout)
        self.nom_entry.grid(row=0, column=1)

        tk.Label(self.frame_ajout, text="Prix:").grid(row=1, column=0)
        self.prix_entry = tk.Entry(self.frame_ajout)
        self.prix_entry.grid(row=1, column=1)

        tk.Label(self.frame_ajout, text="Quantité:").grid(row=2, column=0)
        self.quantite_entry = tk.Entry(self.frame_ajout)
        self.quantite_entry.grid(row=2, column=1)

        if self.type_produit.get() == "electronique":
            tk.Label(self.frame_ajout, text="Garantie (mois):").grid(row=3, column=0)
            self.garantie_entry = tk.Entry(self.frame_ajout)
            self.garantie_entry.grid(row=3, column=1)
        elif self.type_produit.get() == "alimentaire":
            tk.Label(self.frame_ajout, text="Date de péremption:").grid(row=3, column=0)
            self.date_peremption_entry = tk.Entry(self.frame_ajout)
            self.date_peremption_entry.grid(row=3, column=1)

        self.ajouter_btn = tk.Button(self.frame_ajout, text="Ajouter Produit", command=self.ajouter_produit)
        self.ajouter_btn.grid(row=4, columnspan=2, pady=10)

        self.frame_afficher = tk.Frame(self.root)
        self.frame_afficher.pack(pady=10)

        self.afficher_btn = tk.Button(self.frame_afficher, text="Afficher Produits", command=self.afficher_produits)
        self.afficher_btn.pack()

        self.produits_listbox = tk.Listbox(self.frame_afficher, width=50)
        self.produits_listbox.pack()

    def clear_frame(self):
        print("Clearing frame")
        for widget in self.root.winfo_children():
            widget.destroy()

    def ajouter_produit(self):
        print("Adding product")
        nom = self.nom_entry.get()
        prix = float(self.prix_entry.get())
        quantite = int(self.quantite_entry.get())

        if self.type_produit.get() == "electronique":
            garantie = self.garantie_entry.get()
            produit = ProduitElectronique(nom, prix, quantite, garantie)
        elif self.type_produit.get() == "alimentaire":
            date_peremption = self.date_peremption_entry.get()
            produit = ProduitAlimentaire(nom, prix, quantite, date_peremption)

        self.inventaire.ajouter_produit(produit)
        messagebox.showinfo("Succès", "Produit ajouté avec succès!")

    def afficher_produits(self):
        print("Displaying products")
        self.produits_listbox.delete(0, tk.END)
        for produit in self.inventaire.produits:
            self.produits_listbox.insert(tk.END, produit.afficher_info())

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()