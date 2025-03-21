import java.util.Scanner;

public class Personne {
    private String nom;

    public Personne(String nom) {
        this.nom = nom;
    }

    public int compare(Personne P) {
        return this.nom.compareTo(P.nom);
    }

    public String getNom() {
        return this.nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void sePresenter() {
        System.out.println("Je suis une personne et je m'appelle " + this.nom);
    }

    public static void main(String[] args) {
        Personne p1 = new Personne("Alice");
        Personne p2 = new Personne("Bob");

        p1.sePresenter();
        p2.sePresenter();

        System.out.println("Comparaison: " + p1.compare(p2));
    }
}

class Etudiant extends Personne {
    private int code;
    private String universite;
    private double moyenne;

    public Etudiant(String nom, int code, String universite, double moyenne) {
        super(nom);
        this.code = code;
        this.universite = universite;
        this.moyenne = moyenne;
    }

    @Override
    public void sePresenter() {
        System.out.println("Je suis un étudiant à " + this.universite + " et je m'appelle " + this.getNom());
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getUniversite() {
        return universite;
    }

    public void setUniversite(String universite) {
        this.universite = universite;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Etudiant etudiant = (Etudiant) obj;
        return code == etudiant.code;
    }

    public static void main(String[] args) {
        Personne p1 = new Personne("Alice");
        Personne p2 = new Personne("Bob");
        Etudiant e1 = new Etudiant("Charlie", 123, "Université de Paris", 15.5);

        p1.sePresenter();
        p2.sePresenter();
        e1.sePresenter();

        System.out.println("Comparaison: " + p1.compare(p2));

        // Typage dynamique
        Personne p3 = new Etudiant("David", 456, "Université de Lyon", 14.0);
        p3.sePresenter();
    }
}

class GroupeEtudiants {
    private Etudiant[] etudiants;
    private int count;

    public GroupeEtudiants() {
        etudiants = new Etudiant[100];
        count = 0;
    }

    public void ajouterEtudiant(Etudiant e) {
        if (count < 100) {
            etudiants[count++] = e;
        } else {
            System.out.println("Le groupe est plein.");
        }
    }

    public Etudiant rechercherEtudiant(int code) {
        for (int i = 0; i < count; i++) {
            if (etudiants[i].getCode() == code) {
                return etudiants[i];
            }
        }
        return null;
    }

    public void modifierNomEtudiant(int code, String nouveauNom) {
        Etudiant e = rechercherEtudiant(code);
        if (e != null) {
            e.setNom(nouveauNom);
        } else {
            System.out.println("Étudiant non trouvé.");
        }
    }

    public void afficherEtudiants() {
        for (int i = 0; i < count; i++) {
            etudiants[i].sePresenter();
        }
    }

    public double calculerMoyenneGenerale() {
        double somme = 0;
        for (int i = 0; i < count; i++) {
            somme += etudiants[i].getMoyenne();
        }
        return count > 0 ? somme / count : 0;
    }

    public static void main(String[] args) {
        GroupeEtudiants groupe = new GroupeEtudiants();
        Scanner scanner = new Scanner(System.in);
        int choix;

        do {
            System.out.println("1. Ajouter un étudiant");
            System.out.println("2. Rechercher un étudiant par code");
            System.out.println("3. Modifier le nom d'un étudiant");
            System.out.println("4. Afficher tous les étudiants");
            System.out.println("5. Calculer la moyenne générale des étudiants");
            System.out.println("6. Quitter");
            System.out.print("Entrez votre choix: ");
            choix = scanner.nextInt();

            switch (choix) {
                case 1:
                    System.out.print("Nom: ");
                    String nom = scanner.next();
                    System.out.print("Code: ");
                    int code = scanner.nextInt();
                    System.out.print("Université: ");
                    String universite = scanner.next();
                    System.out.print("Moyenne: ");
                    double moyenne = scanner.nextDouble();
                    groupe.ajouterEtudiant(new Etudiant(nom, code, universite, moyenne));
                    break;
                case 2:
                    System.out.print("Code: ");
                    code = scanner.nextInt();
                    Etudiant e = groupe.rechercherEtudiant(code);
                    if (e != null) {
                        e.sePresenter();
                    } else {
                        System.out.println("Étudiant non trouvé.");
                    }
                    break;
                case 3:
                    System.out.print("Code: ");
                    code = scanner.nextInt();
                    System.out.print("Nouveau nom: ");
                    nom = scanner.next();
                    groupe.modifierNomEtudiant(code, nom);
                    break;
                case 4:
                    groupe.afficherEtudiants();
                    break;
                case 5:
                    System.out.println("Moyenne générale: " + groupe.calculerMoyenneGenerale());
                    break;
                case 6:
                    System.out.println("Au revoir!");
                    break;
                default:
                    System.out.println("Choix invalide.");
            }
        } while (choix != 6);

        scanner.close();
    }
}
