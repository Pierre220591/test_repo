# calculs.py

def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait b de a."""
    return a - b

def est_pair(n):
    """Vérifie si un nombre est pair."""
    return n % 2 == 0

def diviser(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible !")
    return a / b

