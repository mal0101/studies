import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from inventaire_classes import Inventaire, ProduitElectronique, ProduitAlimentaire

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de l'Inventaire")
        self.inventaire = Inventaire()
        self.type_produit = tk.StringVar()

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("TRadiobutton", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12, "bold"))

        self.create_type_selection_page()

    def create_type_selection_page(self):
        self.clear_frame()

        frame_type = ttk.Frame(self.root, padding="10")
        frame_type.pack(pady=10)

        ttk.Label(frame_type, text="Choisissez le type de produit:", style="TLabel").pack(pady=5)

        ttk.Radiobutton(frame_type, text="Électronique", variable=self.type_produit, value="electronique", style="TRadiobutton").pack(pady=5)
        ttk.Radiobutton(frame_type, text="Alimentaire", variable=self.type_produit, value="alimentaire", style="TRadiobutton").pack(pady=5)

        ttk.Button(frame_type, text="Suivant", command=self.create_product_info_page, style="TButton").pack(pady=10)

    def create_product_info_page(self):
        self.clear_frame()

        frame_ajout = ttk.Frame(self.root, padding="10")
        frame_ajout.pack(pady=10)

        ttk.Label(frame_ajout, text="Nom:", style="TLabel").grid(row=0, column=0, padx=5, pady=5)
        self.nom_entry = ttk.Entry(frame_ajout)
        self.nom_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_ajout, text="Prix:", style="TLabel").grid(row=1, column=0, padx=5, pady=5)
        self.prix_entry = ttk.Entry(frame_ajout)
        self.prix_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_ajout, text="Quantité:", style="TLabel").grid(row=2, column=0, padx=5, pady=5)
        self.quantite_entry = ttk.Entry(frame_ajout)
        self.quantite_entry.grid(row=2, column=1, padx=5, pady=5)

        if self.type_produit.get() == "electronique":
            ttk.Label(frame_ajout, text="Garantie (mois):", style="TLabel").grid(row=3, column=0, padx=5, pady=5)
            self.garantie_entry = ttk.Entry(frame_ajout)
            self.garantie_entry.grid(row=3, column=1, padx=5, pady=5)
        elif self.type_produit.get() == "alimentaire":
            ttk.Label(frame_ajout, text="Date de péremption:", style="TLabel").grid(row=3, column=0, padx=5, pady=5)
            self.date_peremption_entry = ttk.Entry(frame_ajout)
            self.date_peremption_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame_ajout, text="Ajouter Produit", command=self.ajouter_produit, style="TButton").grid(row=4, columnspan=2, pady=10)

        frame_afficher = ttk.Frame(self.root, padding="10")
        frame_afficher.pack(pady=10)

        ttk.Button(frame_afficher, text="Afficher Produits", command=self.afficher_produits, style="TButton").pack(pady=5)

        self.produits_listbox = tk.Listbox(frame_afficher, width=50, font=("Helvetica", 10))
        self.produits_listbox.pack(pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ajouter_produit(self):
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
        self.produits_listbox.delete(0, tk.END)
        for produit in self.inventaire.produits:
            self.produits_listbox.insert(tk.END, produit.afficher_info())

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()
