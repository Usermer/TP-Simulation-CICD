from app import calculer_moyenne, est_admis, mention
import pytest

def test_calculer_moyenne():
    assert calculer_moyenne([10, 12, 14]) == 12.0
    assert calculer_moyenne([5, 7, 9]) == 7.0


def test_mention():
    assert mention(17) == "Très bien"
    assert mention(15) == "Bien"
    assert mention(13) == "Assez bien"
    assert mention(11) == "Passable"
    assert mention(9) == "Ajourné"

def test_est_admis():
    assert est_admis(12) == True
    assert est_admis(9) == False