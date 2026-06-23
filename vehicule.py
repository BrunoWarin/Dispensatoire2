# vehicule.py - À COMPLÉTER (épreuve flotte)
#
# Hiérarchie Vehicule / VoitureElectrique / Camion, à transposer de la
# hiérarchie Livre / LivreNumerique / LivreAudio (S11-S18).
# Pour cette épreuve, aucune docstring n'est demandée : les indices «#»
# donnent le RÔLE (et parfois le cas analogue à transposer), et les
# tests (test_vehicule.py) fixent les valeurs et exceptions exactes.
# Complétez les corps « ... ».


class Vehicule:

    def __init__(self, marque, modele, numero_chassis, nb_places, annee):
        """Initialise un véhicule en validant ses caracteristiques.

        Args:
            marque (str): Marque du vehicule 
            modele (str): Modele du vehicule
            numero_chassis (int): Numero de chassis du vehicule
            nb_places (int): Nombre de places du vehicule
            annee (int): Annee de fabrication du vehicule

        Raises:
            TypeError: Si la marque n'est pas une chaine de caractere
            TypeError: Si le modele n'est pas une chaine de caractere 
            TypeError: Si le numero de chassis n'est pas un nombre entier 
            TypeError: Si le numero de place n'est pas un numero
            TypeError: Si l'annee n'est pas un numero 
        """
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


    @staticmethod
    def chassis_valide(chaine):
        """Verifie que le numero de chassis est valide

        Args:
            chaine (str(ou int)): Numero de chassis de la voiture 

        Raises:
            ValueError: Le numero de chassis ne comprend pas 17 caractere
            TypeError: Le numero de chassis n'est pas compose de chiffres ou de lettres

        Returns:
            bool: True si le numero de chassis est valide, False si ce n'est pas le cas
        """
        if chaine != 17:
            raise ValueError ("Le numero de chassis doit commprendre 17 caracteres")
        if not isinstance (chaine,str) or isinstance (chaine, bool) or not isinstance (chaine,str):
            raise TypeError("le numero de chassis doit etre compose de numéros et de lettres.")
            return False 
        chaine == True 
        


    @classmethod
    def depuis_csv(cls, ligne):
        """Cree une voiture a partir d'une ligne csv.

        Args:
            ligne (str): Ligne au format 
            marque, modele, numero_chassis, nb_places, annee, disponible 

        Raises:
            ValueError: Si le champ ne compte pas 6 elements

        Returns:
            _type_: Une voiture avec des nouvelles valeurs.
        """
        champs = ligne.split(";")
        if len(champs) != 6:
            raise ValueError(
                "La ligne doit contenir exactement 6 champs séparés "
                "par des points-virgules."
            )
        marque, modele, numero_chassis, nb_places, annee, disponible = champs
        return cls(marque, modele, numero_chassis, int(nb_places), int(annee), bool(disponible))


    def to_dict(self):
        """Serialise un vehicule en dictionnaire compartible avec JSON

        Returns:
            dict: Dictionnaire avec les donnees du vehicule.
        """
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
        """Reconstruit un vehicule a partir d'un dictionnaire.

        Args:
            donnees (dict): Dictionnaire produit par to_dict

        Returns:
            Vehicule: Equivalent au vehicule qui a ete serialise
        """
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
        if not donnees.get("disponible", True):
            vehicule.emprunter()


    def louer(self):
        """Loue un vehicule disponible

        Raises:
            ValueError: Si le vehicule est deja loue
        """
        if not self._disponible:
            raise ValueError("Vehicule deja loue")
        self._disponible = False

    def restituer(self):
        """Restitue un vehicule loué

        Raises:
            ValueError: Si le Vehicule est deja disponible
        """
        if self._disponible:
            raise ValueError("Vehicule déjà disponible")
        self._disponible = True


    def fiche_resume(self):
        """Affiche un resume de l'etat du vehicule.

        Returns:
            str: Resume de l'ett du vehicule 
        """
        return (f"{self.marque} {self.modele} {hash(self.numero_chassis)}"
                f"{self.nb_places} {self.annee}"
                )


    def __str__(self):
        """Affichage compréhensible pour l'utilisateur du vehicule 

        Returns:
            str: affichage comprehensible du vehicule 
        """
        return f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}"
    def __repr__(self):
        """Affichage non ambigue du vehicule 

        Returns:
            str: affichage non ambigue du vehicule.
        """
        return(f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
        )


    def __eq__(self, autre):
        """Egalite par numero de chassis

        Args:
            autre (int): numero de chassis

        Returns:
            bool: True si les numeros de chassis correspondent, sinon False.
        """
        if not isinstance(autre, self.numero_chassis):
            return NotImplemented
        return self.numero_chassis == autre.numero_chassis

    def __hash__(self):
        """Hash le numero de chassis.

        Returns:
            hash: representation hash du numero de chassis.
        """
        return hash(self.numero_chassis)


class VoitureElectrique(Vehicule):

    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 autonomie_km):
        """Initialise une voiture electrique 

        Args:
            marque (str): Marque de la voiture
            modele (str): Modele de la voiture 
            numero_chassis (int): Numero de chassis de la voiture 
            nb_places (int): Nombre de places de la voiture
            annee (int): Annee de fabrication de la voiture 
            autonomie_km (int): Autonomie electrique en km de la voiture 

        Raises:
            TypeError: Si l'autonomie n'est pas un chiffre entier
            ValueError: Si l'autonomie n'est pas un entier positif
        """
        super.__init__(marque=marque, modele=modele, numero_chassis=numero_chassis, nb_places= nb_places, annee= annee)
        if not isinstance(autonomie_km, int) or isinstance (autonomie_km, bool):
            TypeError("L'autonomie doit être un chiffre entier")
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
        """Cree une voiture electrique a partir d'une ligne CSV a 7 champs.

        Args:
            ligne (str): ligne au format:
            marque, modele, numero_chassis, nb_places, annee, disponible, autonomie

        Raises:
            ValueError: Si la ligne ne contient pas 7 elementS

        Returns:
            VoitureElectrique: Initialisation d'une nouvelle voiture electrique.
        """
        champs = ligne.split(";")
        if len(champs) != 7:
            raise ValueError(
                "La ligne doit contenir exactement 7 champs séparés "
                "par des points-virgules."
            )
        marque, modele, numero_chassis, nb_places, annee, disponible, autonomie = champs
        return cls(marque, modele, numero_chassis, int(nb_places), int(annee), bool(disponible), int(autonomie))

    def to_dict(self):
        """Enrichit le dictionnaire parent avec l'autonomie en km 

        Returns:
            dict: Dictionnaire de la voiture electrique
        """
        donnees = super().to_dict()
        donnees["type"] = "VoitureElectrique"
        donnees["Autonomie km"] = self.autonomie_km
        return donnees

    @classmethod
    def from_dict(cls, donnees):
        """Reconstruit une voiture electrique a partir d'un dictionnaire 

        Args:
            donnees (dict): Dictionnaire produit par to_dict

        Returns:
            VoitureElectrique: Une voiture electrique.
        """
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
        ...

    def __str__(self):
        """Retourne une représentation comprehensible pour l'utilisateur 
        """
        return(f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}, {self.autonomie_km}")

    def __repr__(self):
        """Retourne un affichage non ambigue de la voiture electrique
        """
        return (f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
               f"Autonomie : {self.autonomie_km}"
        )


class Camion(Vehicule):


    def __init__(self, marque, modele, numero_chassis, nb_places, annee,
                 charge_utile_t):
        """Initialise un camion

        Args:
            marque (str): Marque de la voiture
            modele (str): Modele de la voiture 
            numero_chassis (int): Numero de chassis de la voiture 
            nb_places (int): Nombre de places de la voiture
            annee (int): Annee de fabrication de la voiture 
            Charge utile (float): Charge utile du camion 

        Raises:
            TypeError: Si la charge utile n'est pas un chiffre
            ValueError: Si la charge utile est inférieure à 0 
        """
        super.__init__(marque=marque, modele=modele, numero_chassis=numero_chassis, nb_places=nb_places, annee=annee)
        if not isinstance(charge_utile_t, float) or isinstance(charge_utile_t,bool):
            raise TypeError("La charge utile doit être un chiffre")
        if charge_utile_t < 0: 
            raise ValueError("La charge utile doit etre plsu grande que 0")
        self.charge_utile_t = charge_utile_t

    @property
    def charge_utile_t(self):
        """Retourne la charge utile 

        Returns:
            float: Charge utile du camion.
        """
        return self.charge_utile_t

    @classmethod
    def depuis_csv(cls, ligne):
        """Crée un Camion à partir d'une ligne CSV à 7 champs.

        Args:
            ligne (str): Ligne au format
            marque, modele, numero_chassis, nb_places, annee, disponible, charge_utile_t

        Raises:
            ValueError: Si la ligne ne contient pas 7 elements 

        Returns:
            Camion: Initialisation d'un camion
        """
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
        """Enrichit le dictionnaire parent en ajoutant la charge utile 

        Returns:
            dict: Dictionnaire du camion
        """
        donnees = super().to_dict()
        donnees["type"] = "Camion"
        donnees["Charge utile"] = self.charge_utile_t
        return donnees

    @classmethod
    def from_dict(cls, donnees):
        """Reconstruit un camion a partir du dictionnaire.

        Args:
            donnees (dict): Dictionnaire construit par to_dict

        Returns:
            Camion: Un camion 
        """
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
        ...

    def __str__(self):
        """Representation d'un camion comprenhensible par l'utilisateur.
        """
        return f"{self.marque}, {self.modele}, {hash(self.numero_chassis)}, {self.nb_places}, {self.annee}, {self.charge_utile_t}"

    def __repr__(self):
        """Representation non ambigue d'un camion
        """
        return (f"Marque : {self.marque} - Modele : {self.modele}"
               f" Annee : {self.annee} - Numero de chassis {self.numero_chassis}"
               f"Nombre de places {self.nb_places} - Disponibilité {self.disponible}"
               f"Charge utile : {self.charge_utile_t}"
        )