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

    def __init__(self, marque, modele, numero_chassis, nb_places, annee):
        if not isinstance (marque, str):
            raise TypeError("Le nom de la marque doit être une chaine de caractere ")
        if not isinstance(modele, str):
            raise TypeError("Le modele doit être une chaine de caractere")
        if not isinstance (numero_chassis, int) or isinstance (numero_chassis,bool):
            raise TypeError ("Le numéro de chassis doit être un numero")
        if not isinstance (nb_places, int) or isinstance (nb_places,bool):
            raise TypeError ("Le numéro de places doit être un numero")
        if not isinstance (annee, int) or isinstance (annee,bool):
            raise TypeError ("L'année doit être un numero")
        self._marque = marque
        self._modele = modele 
        self._numero_chassis = numero_chassis
        self._nb_places = nb_places
        self._annee = annee 
        self._disponible = True

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
        return self._disponible

    # --- Méthode statique ---

    @staticmethod
    def chassis_valide(chaine):
        # Vrai si la chaîne a exactement la bonne longueur et n'est faite
        # que de caractères alphanumériques. Longueur et nature exactes :
        # déductibles des tests. Une entrée non-str renvoie False.
        if chaine != 17:
            raise ValueError ("Le numero de chassis doit commprendre 17 caracteres")
        if not isinstance (chaine,str) or isinstance (chaine, bool) or not isinstance (chaine,str):
            raise TypeError("le numero de chassis doit etre compose de numéros et de lettres.")
            return False 
        chaine == True 
        

    # --- Constructeur alternatif ---

    @classmethod
    def depuis_csv(cls, ligne):
        # Découper la ligne, vérifier le nombre de champs, construire via
        # cls(...). Même rôle que Livre.depuis_chaine_csv : utiliser cls
        # (et non Vehicule) est ce qui donnera le TYPE EXACT dans les
        # sous-classes.
        champs = ligne.split(";")
        if len(champs) != 6:
            raise ValueError(
                "La ligne doit contenir exactement 6 champs séparés "
                "par des points-virgules."
            )
        marque, modele, numero_chassis, nb_places, annee, disponible = champs
        return cls(marque, modele, numero_chassis, int(nb_places), int(annee), bool(disponible))

    # --- Sérialisation JSON ---

    def to_dict(self):
        # Produire un dict marqué d'un champ « type » (le discriminateur
        # qui guidera la reconstruction). Clés attendues : voir les tests.
        return {
            "type": "Vehicule",
            "Marque": self.marque,
            "Modele": self.modele,
            "Numero de chassis": self.numero_chassis,
            "nb_places": self.nb_places,
            "annee": self._annee,
            "disponible": self._disponible,
        }

    @classmethod
    def from_dict(cls, donnees):
        # Pendant de to_dict : reconstruire via cls(...), puis restaurer la
        # disponibilité par l'API publique (jamais en écrivant l'attribut
        # privé). Même logique que Livre.from_dict.
        Vehicule = cls(
            donnees["Marque"],
            donnees["Modele"],
            donnees["Numero de chassis"],
            donnees["nb_places"],
            donnees["annee"],
            donnees["disponible"]
        )
        Vehicule._restaurer_disponibilite(Vehicule, donnees)
        return Vehicule

    @staticmethod
    def _restaurer_disponibilite(vehicule, donnees):
        """Restaure la disponibilite d'un vehicule 

        Args:
            vehicule (str): Le vehicule 
            donnees (_type_): _description_
            disponible (_type_): _description_
        """
        # Si l'objet était loué, le replacer dans cet état via la méthode
        # métier. Factorisé : toutes les sous-classes restaurent pareil.
        if not donnees.get("disponible", True):
            vehicule.emprunter()


    # --- Méthodes métier ---

    def louer(self):
        # Bascule vers « loué » ; refuser si déjà loué.
        if not self._disponible:
            raise ValueError("Vehicule deja loue")
        self._disponible = False

    def restituer(self):
        # Bascule vers « disponible » ; refuser si déjà disponible.
        if self._disponible:
            raise ValueError("Vehicule déjà disponible")
        self._disponible = True


    def fiche_resume(self):
        # Description de la capacité d'un véhicule générique. Format exact :
        # voir les tests. (Transposé de Livre.taille_estimee.)
        return (f"{self.marque} {self.modele} {hash(self.numero_chassis)}"
                f"{self.nb_places} {self.annee}"
                )

    # --- Représentations ---

    def __str__(self):
        return f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}"
    def __repr__(self):
        return(f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
        )

    # --- Identité (entité) ---

    def __eq__(self, autre):
        # Vehicule est une ENTITE : égalité par numéro de châssis (comme
        # Livre par ISBN). NotImplemented si « autre » n'est pas un Vehicule.
        if not isinstance(autre, self.numero_chassis):
            return NotImplemented
        return self.numero_chassis == autre.numero_chassis

    def __hash__(self):
        # Cohérent avec __eq__ : fondé sur le châssis.
        return hash(self.numero_chassis)


class VoitureElectrique(Vehicule):
    # Enrichit Vehicule d'une autonomie. Transposé de LivreNumerique.

    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 autonomie_km):
        super.__init__(marque=marque, modele=modele, numero_chassis=numero_chassis, nb_places= nb_places, annee= annee)
        if not isinstance(autonomie_km, int) or isinstance (autonomie_km, bool):
            TypeError("L'autonome doit être un chiffre entirer")
        if autonomie_km < 0: 
            ValueError("L'autonomie doit etre un entier positif")
        self._autonomie_km = autonomie_km 

    @property
    def autonomie_km(self):
        """Retourne l'autonomie de la voiture.

        Returns:
            int: Autonomie de la voiture.
        """
        return self._autonomie_km

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Vehicule.depuis_csv, mais un champ de plus (l'autonomie).
        champs = ligne.split(";")
        if len(champs) != 7:
            raise ValueError(
                "La ligne doit contenir exactement 7 champs séparés "
                "par des points-virgules."
            )
        marque, modele, numero_chassis, nb_places, annee, disponible, autonomie = champs
        return cls(marque, modele, numero_chassis, int(nb_places), int(annee), bool(disponible), int(autonomie))

    def to_dict(self):
        # ENRICHIR le dictionnaire hérité du parent (ne pas le réécrire) :
        # corriger « type » et ajouter l'attribut propre. (Geste de
        # LivreNumerique.to_dict.)
        donnees = super().to_dict()
        donnees["type"] = "VoitureElectrique"
        donnees["Autonomie km"] = self.autonomie_km
        return donnees

    @classmethod
    def from_dict(cls, donnees):
        VoitureElectrique = cls(
            donnees["Marque"],
            donnees["Modele"],
            donnees["Numero de chassis"],
            donnees["nb_places"],
            donnees["annee"],
            donnees["disponible"],
            donnees["Autonomie km"]
        )
        Vehicule._restaurer_disponibilite(Vehicule, donnees)
        return Vehicule

    def fiche_resume(self):
        # On REPREND la fiche de base et on la complète : la capacité reste
        # un préfixe (ENRICHISSEMENT). Format exact : voir les tests.
        ...

    def __str__(self):
        return(f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}, {self.autonomie_km}")

    def __repr__(self):
        return (f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
               f"Autonomie : {self.autonomie_km}"
        )


class Camion(Vehicule):
    # La mesure pertinente est la charge utile, pas le nombre de places.
    # Transposé de LivreAudio (durée d'écoute plutôt que pages).

    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 charge_utile_t):
        # Déléguer au parent, puis valider l'attribut propre (charge :
        # nombre strictement positif, stocké en float
        super.__init__(marque=marque, modele=modele, numero_chassis=numero_chassis, nb_places=nb_places, annee=annee)
        if not isinstance(charge_utile_t, float) or isinstance(charge_utile_t,bool):
            raise TypeError("La charge utile doit être un chiffre")
        if charge_utile_t < 0: 
            raise ValueError("La charge utile doit etre plsu grande que 0")
        self.charge_utile_t = charge_utile_t

    @property
    def charge_utile_t(self):
        return self.charge_utile_t

    @classmethod
    def depuis_csv(cls, ligne):
        champs = ligne.split(";")
        if len(champs) != 7:
            raise ValueError(
                "La ligne doit contenir exactement 6 champs séparés "
                "par des points-virgules."
            )
        marque, modele, numero_chassis, nb_places, annee, disponible, charge_utile_t = champs
        return cls(
            marque, modele, numero_chassis,
            int(nb_places), int(annee), bool(disponible), float(charge_utile_t)
            )

    def to_dict(self):
        donnees = super().to_dict()
        donnees["type"] = "Camion"
        donnees["Charge utile"] = self.charge_utile_t
        return donnees

    @classmethod
    def from_dict(cls, donnees):
        Camion = cls(
            donnees["Marque"],
            donnees["Modele"],
            donnees["Numero de chassis"],
            donnees["nb_places"],
            donnees["annee"],
            donnees["disponible"],
            donnees["Charge utile"]
        )

    def fiche_resume(self):
        # Ici la mesure pertinente n'est PAS le nombre de places : on ne
        # réutilise donc PAS la fiche de base (REMPLACEMENT). Format exact :
        # voir les tests.
        ...

    def __str__(self):
        return f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}, {self.charge_utile_t}"

    def __repr__(self):
        return (f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
               f"Charge utile : {self.charge_utile_t}"
        )