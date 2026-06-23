# tarif.py - À COMPLÉTER (épreuve flotte)
#
# Objet-valeur Tarif, à transposer de l'objet-valeur Argent (S11).
# Pour cette épreuve, aucune docstring n'est demandée : les indices «#»
# donnent le ROLE, et les tests (test_tarif.py) fixent les valeurs
# exactes, l'ordre et les exceptions. Complétez les corps « ... ».

from functools import total_ordering


@total_ordering
class Tarif:
    # Objet-valeur IMMUABLE : l'égalité ET l'ordre portent sur la VALEUR
    # (montant + devise), pas sur l'identité mémoire. C'est le contraste
    # avec Vehicule, qui est une entité (identité par châssis).

    def __init__(self, montant, devise="EUR"):
        """Initialise un tarif 

        Args:
            montant (int): Montant
            devise (str, optional): Devise du montant. Defaults to "EUR".

        Raises:
            TypeError: La devise doit etre une chaine de caractere
            TypeError: Le montant doit être un chiffre
            ValueError: Le montant doit être plus grand que 0
        """
        # Refuser un montant strictement négatif ; stocker le montant en float.
        if not isinstance (devise, str):
            raise TypeError("La devise doit etre une chaine de caractere")
        if not isinstance (montant, int) or isinstance (montant, bool):
            raise TypeError("Le montant doit être un chiffre")
        if montant < 0: 
            raise ValueError("Le montant doit être plus grand que 0")
        self._montant = montant
        self._devise = devise 

    @property
    def montant(self):
        """Retourne le montant

        Returns:
            int: Le montant
        """
        return self._montant

    @property
    def devise(self):
        """Retourne la devise 

        Returns:
            str: Devise du montant
        """
        return self._devise 

    def __eq__(self, autre):
        """Verifie l'eglite entre deux montants et deux devises

        Args:
            autre (): 

        Raises:
            ValueError: Si les deux devises sont différentes.

        Returns:
            bool: True si les deux montants correspondent, sinon False.
        """
        if not isinstance(autre,Tarif):
            return NotImplemented
        if not self.devise == autre.devise:
            raise ValueError("On ne peut pas comparer des devises différentes")
        return self.montant == autre.montant

    def __hash__(self):
        """Rend l'objet hachable de façon cohérent avec __eq__
        """
        return hash(self.montant, self.devise)

    def __lt__(self, autre):
        if not isinstance(autre,Tarif):
            return NotImplemented
        if not self.devise == autre.devise:
            raise ValueError("On ne peut pas comparer des devises différentes")
        return self.montant < autre.montant


    def __add__(self, autre):
        if not isinstance(autre,Tarif):
            return NotImplemented
        if not self.devise == autre.devise:
            raise ValueError("On ne peut pas comparer des devises différentes")
        return Tarif(self.montant + autre.montant, self.devise)
        ...

    def __str__(self):
        return f"{self.montant} {self.devise}"

    def __repr__(self):
        return f"Argent({self.montant},{self.devise})"
