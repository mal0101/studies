import java.util.ArrayList;
import java.util.List;



class SallePleineException extends Exception {
    private Spectateur spectateur;

    public SallePleineException(Spectateur spectateur) {
        super("La salle est pleine !");
        this.spectateur = spectateur;
    }

    public Spectateur getSpectateur() {
        return spectateur;
    }
}

class Spectateur {
    private String nom;

    public Spectateur(String nom) {
        this.nom = nom;
    }

    public String getNom() {
        return nom;
    }
}

class Salle {
    private int capacite;
    private List<Spectateur> spectateurs;

    public Salle(int capacite) {
        this.capacite = capacite;
        this.spectateurs = new ArrayList<>();
    }

    public void ajouterSpectateur(Spectateur spectateur) throws SallePleineException {
        if (spectateurs.size() >= capacite) {
            throw new SallePleineException(spectateur);
        }
        spectateurs.add(spectateur);
    }

    public int getCapacite() {
        return capacite;
    }

    public int getNombreSpectateurs() {
        return spectateurs.size();
    }
}

class Cinema {
    private int capaciteSalle;
    private List<Salle> salles;

    public Cinema(int capaciteSalle) {
        this.capaciteSalle = capaciteSalle;
        this.salles = new ArrayList<>();
        this.salles.add(new Salle(capaciteSalle)); 
    }

    public void placer(Spectateur spectateur) {
        Salle derniereSalle = salles.get(salles.size() - 1);
        try {
            derniereSalle.ajouterSpectateur(spectateur);
        } catch (SallePleineException e) {
            Salle nouvelleSalle = new Salle(capaciteSalle);
            salles.add(nouvelleSalle);
            try {
                nouvelleSalle.ajouterSpectateur(spectateur);
            } catch (SallePleineException ex) {
                ex.printStackTrace();
            }
        }
    }

    public int getNombreSalles() {
        return salles.size();
    }
}
