# vehicule.py - À COMPLÉTER (épreuve flotte)
#
# Hiérarchie Vehicule / VoitureElectrique / Camion, à transposer de la
# hiérarchie Livre / LivreNumerique / LivreAudio (S11-S18).
# Pour cette épreuve, aucune docstring n'est demandée : les indices «#»
# donnent le RÔLE (et parfois le cas analogue à transposer), et les
# tests (test_vehicule.py) fixent les valeurs et exceptions exactes.
# Complétez les corps « ... ».


class Vehicule:
    # ENTITE largement immuable. Identité métier : le numéro de châssis
    # (qui ne change jamais, contrairement à la plaque). Seule la
    # disponibilité évolue. Transposé de Livre (identité par ISBN).

    def __init__(self, marque, modele, numero_chassis, nb_places, annee, disponible):
        if not isinstance (marque, str):
            TypeError("Le nom de la marque doit être une chaine de caractere ")
        if not isinstance(modele, str):
            TypeError("Le modele doit être une chaine de caractere")
        if not isinstance (numero_chassis, int) or isinstance (numero_chassis,bool):
            TypeError ("Le numéro de chassis doit être un numero")
        if not isinstance (nb_places, int) or isinstance (nb_places,bool):
            TypeError ("Le numéro de places doit être un numero")
        if not isinstance (annee, int) or isinstance (annee,bool):
            TypeError ("L'année doit être un numero")
        self._marque = marque
        self._modele = modele 
        self._numero_chassis = numero_chassis
        self._nb_places = nb_places
        self._annee = annee 
        disponible == True

    @property
    def marque(self):
        """Retourne la marque de la voiture.

        Returns:
            str: Marque de la voiture.
        """
        return self._marque

    @property
    def modele(self):
        """Retourne le modele de la voiture 

        Returns:
            str: Modele de la voiture.
        """
        return self._modele

    @property
    def numero_chassis(self):
        """Retourne le numero de chassis

        Returns:
            str: numero de chassis
        """
        return self._numero_chassis

    @property
    def nb_places(self):
        """Retourne le nombre de places

        Returns:
            int: Nombre de places.
        """
        return self._nb_places

    @property
    def annee(self):
        """Retourne l'annee de la voiture

        Returns:
            int: Annee de la voiture 
        """
        return self._annee

    @property
    def disponible(self):
        """Retourne la disponibilite de la voiture 

        Returns:
            bool: Disponibilité de la voiture.
        """
        return self.disponible

    # --- Méthode statique ---

    @staticmethod
    def chassis_valide(chaine):
        # Vrai si la chaîne a exactement la bonne longueur et n'est faite
        # que de caractères alphanumériques. Longueur et nature exactes :
        # déductibles des tests. Une entrée non-str renvoie False.
        ...

    # --- Constructeur alternatif ---

    @classmethod
    def depuis_csv(cls, ligne):
        # Découper la ligne, vérifier le nombre de champs, construire via
        # cls(...). Même rôle que Livre.depuis_chaine_csv : utiliser cls
        # (et non Vehicule) est ce qui donnera le TYPE EXACT dans les
        # sous-classes.
        ...

    # --- Sérialisation JSON ---

    def to_dict(self):
        # Produire un dict marqué d'un champ « type » (le discriminateur
        # qui guidera la reconstruction). Clés attendues : voir les tests.
        ...

    @classmethod
    def from_dict(cls, donnees):
        # Pendant de to_dict : reconstruire via cls(...), puis restaurer la
        # disponibilité par l'API publique (jamais en écrivant l'attribut
        # privé). Même logique que Livre.from_dict.
        ...

    @staticmethod
    def _restaurer_disponibilite(vehicule, donnees):
        # Si l'objet était loué, le replacer dans cet état via la méthode
        # métier. Factorisé : toutes les sous-classes restaurent pareil.
        ...

    # --- Méthodes métier ---

    def louer(self):
        # Bascule vers « loué » ; refuser si déjà loué.
        ...

    def restituer(self):
        # Bascule vers « disponible » ; refuser si déjà disponible.
        ...

    def fiche_resume(self):
        # Description de la capacité d'un véhicule générique. Format exact :
        # voir les tests. (Transposé de Livre.taille_estimee.)
        ...

    # --- Représentations ---

    def __str__(self):
        ...

    def __repr__(self):
        ...

    # --- Identité (entité) ---

    def __eq__(self, autre):
        # Vehicule est une ENTITE : égalité par numéro de châssis (comme
        # Livre par ISBN). NotImplemented si « autre » n'est pas un Vehicule.
        ...

    def __hash__(self):
        # Cohérent avec __eq__ : fondé sur le châssis.
        ...


class VoitureElectrique(Vehicule):
    # Enrichit Vehicule d'une autonomie. Transposé de LivreNumerique.

    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 autonomie_km):
        # Déléguer la validation héritée au parent, puis valider l'attribut
        # propre (autonomie : entier strictement positif).
        ...

    @property
    def autonomie_km(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Vehicule.depuis_csv, mais un champ de plus (l'autonomie).
        ...

    def to_dict(self):
        # ENRICHIR le dictionnaire hérité du parent (ne pas le réécrire) :
        # corriger « type » et ajouter l'attribut propre. (Geste de
        # LivreNumerique.to_dict.)
        ...

    @classmethod
    def from_dict(cls, donnees):
        ...

    def fiche_resume(self):
        # On REPREND la fiche de base et on la complète : la capacité reste
        # un préfixe (ENRICHISSEMENT). Format exact : voir les tests.
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...


class Camion(Vehicule):
    # La mesure pertinente est la charge utile, pas le nombre de places.
    # Transposé de LivreAudio (durée d'écoute plutôt que pages).

    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 charge_utile_t):
        # Déléguer au parent, puis valider l'attribut propre (charge :
        # nombre strictement positif, stocké en float).
        ...

    @property
    def charge_utile_t(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        ...

    def to_dict(self):
        ...

    @classmethod
    def from_dict(cls, donnees):
        ...

    def fiche_resume(self):
        # Ici la mesure pertinente n'est PAS le nombre de places : on ne
        # réutilise donc PAS la fiche de base (REMPLACEMENT). Format exact :
        # voir les tests.
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...
