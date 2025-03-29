
class ValRayonValideException extends Exception {
    public ValRayonValideException(String message) {
        super(message);
    }
}


class CouleurValideException extends Exception {
    public CouleurValideException(String message) {
        super(message);
    }
}

public class Cercle {
    private double x, y, rayon;
    private String couleur; 

  
    public Cercle(double x, double y, double rayon, String couleur) throws ValRayonValideException, CouleurValideException {
        this.x = x;
        this.y = y;
        setRayon(rayon);
        setCouleur(couleur);
    }

   
    public double getRayon() {
        return rayon;
    }

    
    public String getCouleur() {
        return couleur;
    }

   
    public void setRayon(double newRayon) throws ValRayonValideException {
        if (newRayon < 0) {
            throw new ValRayonValideException("Le rayon ne peut pas être négatif. Initialisation à son opposé.");
        }
        this.rayon = newRayon;
    }

    
    public void setCouleur(String newCouleur) throws CouleurValideException {
        if (newCouleur == null || newCouleur.isEmpty() || newCouleur.equalsIgnoreCase("rouge")) {
            throw new CouleurValideException("Couleur invalide : elle ne peut pas être nulle, vide ou rouge.");
        }
        this.couleur = newCouleur;
    }

   
    @Override
    public String toString() {
        return "Cercle [Centre=(" + x + ", " + y + "), Rayon=" + rayon + ", Couleur=" + couleur + "]";
    }

   
    public static void main(String[] args) {
        try {
            Cercle c1 = new Cercle(0, 0, 5, "bleu");
            System.out.println(c1);

            c1.setRayon(-10); // This will throw an exception
        } catch (ValRayonValideException e) {
            System.out.println("Exception capturée : " + e.getMessage());
        } catch (CouleurValideException e) {
            System.out.println("Exception capturée : " + e.getMessage());
        }

        try {
            Cercle c2 = new Cercle(1, 1, 10, "rouge"); // This will throw an exception
        } catch (ValRayonValideException e) {
            System.out.println("Exception capturée : " + e.getMessage());
        } catch (CouleurValideException e) {
            System.out.println("Exception capturée : " + e.getMessage());
        }
    }
}