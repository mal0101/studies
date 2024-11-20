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

        self.create_main_page()

    def create_main_page(self):
        self.clear_frame()

        frame_main = ttk.Frame(self.root, padding="10")
        frame_main.pack(pady=10)

        ttk.Label(frame_main, text="Choisissez le type de produit:", style="TLabel").pack(pady=5)

        ttk.Radiobutton(frame_main, text="Électronique", variable=self.type_produit, value="electronique", style="TRadiobutton").pack(pady=5)
        ttk.Radiobutton(frame_main, text="Alimentaire", variable=self.type_produit, value="alimentaire", style="TRadiobutton").pack(pady=5)

        ttk.Label(frame_main, text="Nom:", style="TLabel").pack(pady=5)
        self.nom_entry = ttk.Entry(frame_main)
        self.nom_entry.pack(pady=5)

        ttk.Label(frame_main, text="Prix:", style="TLabel").pack(pady=5)
        self.prix_entry = ttk.Entry(frame_main)
        self.prix_entry.pack(pady=5)

        ttk.Label(frame_main, text="Quantité:", style="TLabel").pack(pady=5)
        self.quantite_entry = ttk.Entry(frame_main)
        self.quantite_entry.pack(pady=5)

        self.extra_entry_label = ttk.Label(frame_main, style="TLabel")
        self.extra_entry_label.pack(pady=5)
        self.extra_entry = ttk.Entry(frame_main)
        self.extra_entry.pack(pady=5)

        ttk.Button(frame_main, text="Ajouter Produit", command=self.ajouter_produit, style="TButton").pack(pady=10)
        ttk.Button(frame_main, text="Afficher Produits", command=self.afficher_produits, style="TButton").pack(pady=5)

        self.produits_listbox = tk.Listbox(frame_main, width=50, font=("Helvetica", 10))
        self.produits_listbox.pack(pady=5)

        self.type_produit.trace("w", self.update_extra_entry)

    def update_extra_entry(self, *args):
        if self.type_produit.get() == "electronique":
            self.extra_entry_label.config(text="Garantie (mois):")
        elif self.type_produit.get() == "alimentaire":
            self.extra_entry_label.config(text="Date de péremption:")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ajouter_produit(self):
        nom = self.nom_entry.get()
        prix = float(self.prix_entry.get())
        quantite = int(self.quantite_entry.get())

        if self.type_produit.get() == "electronique":
            garantie = self.extra_entry.get()
            produit = ProduitElectronique(nom, prix, quantite, garantie)
        elif self.type_produit.get() == "alimentaire":
            date_peremption = self.extra_entry.get()
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
