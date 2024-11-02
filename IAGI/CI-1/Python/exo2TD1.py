# Exercice 2:

import re
from collections import Counter   
   
 # Fonction pour analyser un texte
def analyser_texte(texte):
        # Analyse lexicale
        mots = re.findall(r'\b\w+\b', texte.lower())
        frequences = Counter(mots)
        mots_uniques = set(mots)
        palindromes = [mot for mot in mots_uniques if mot == mot[::-1]]

        # Analyse grammaticale
        phrases = re.split(r'[.!?]', texte)
        phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
        longueur_phrases = [len(phrase.split()) for phrase in phrases]
        ponctuations = re.findall(r'[.!?]', texte)
        types_mots = Counter(re.findall(r'\b\w+\b', texte))

        # Rapports
        top_10_mots = frequences.most_common(10)
        phrases_longues = sorted(phrases, key=lambda x: len(x.split()), reverse=True)[:10]
        diversite_vocabulaire = len(mots_uniques) / len(mots) if mots else 0
        patterns_repetitifs = [mot for mot, count in frequences.items() if count > 1]

        return {
            'frequences': frequences,
            'mots_moins_utilises': [mot for mot, count in frequences.items() if count == 1],
            'palindromes': palindromes,
            'nombre_phrases': len(phrases),
            'longueur_phrases': longueur_phrases,
            'types_ponctuation': Counter(ponctuations),
            'statistiques_types_mots': types_mots,
            'top_10_mots': top_10_mots,
            'phrases_longues': phrases_longues,
            'diversite_vocabulaire': diversite_vocabulaire,
            'patterns_repetitifs': patterns_repetitifs
        }

    # Fonction pour afficher le rapport d'analyse
def afficher_rapport(rapport):
        print("\n--- Analyse Lexicale ---")
        print("Fréquence des mots:", rapport['frequences'])
        print("Mots les moins utilisés:", rapport['mots_moins_utilises'])
        print("Palindromes:", rapport['palindromes'])

        print("\n--- Analyse Grammaticale ---")
        print("Nombre de phrases:", rapport['nombre_phrases'])
        print("Longueur des phrases:", rapport['longueur_phrases'])
        print("Types de ponctuation utilisés:", rapport['types_ponctuation'])
        print("Statistiques par type de mot:", rapport['statistiques_types_mots'])

        print("\n--- Rapports ---")
        print("Top 10 des mots:", rapport['top_10_mots'])
        print("Phrases les plus longues:", rapport['phrases_longues'])
        print("Diversité du vocabulaire:", rapport['diversite_vocabulaire'])
        print("Patterns répétitifs:", rapport['patterns_repetitifs'])

    # Menu pour l'analyse de texte
def menu_analyse_texte():
        texte = input("Entrez le texte à analyser: ")
        rapport = analyser_texte(texte)
        afficher_rapport(rapport)

    # Exécution du menu d'analyse de texte
menu_analyse_texte()