# test_calculs.py
import pytest
from calculs import addition, soustraction, est_pair, diviser

def test_addition():
    """Teste la fonction addition."""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    """Teste la fonction soustraction."""
    assert soustraction(5, 3) == 2
    assert soustraction(10, 10) == 0

def test_est_pair():
    """Teste la fonction est_pair."""
    assert est_pair(2) == True
    assert est_pair(3) == False
    assert est_pair(0) == True

def test_diviser():
    """Teste la fonction diviser."""
    assert diviser(10, 2) == 5
    assert diviser(5, 2) == 2.5
    
    # Test qu'une exception est levée pour une division par zéro
    with pytest.raises(ValueError):
        diviser(10, 0)

