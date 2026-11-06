import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_soustraction():
    """Test de base : 10 - 4 = 6."""
    response = client.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json()["result a-b="] == 6


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 4, 6),               # cas normal
        (4, 10, -6),              # résultat négatif
        (5, 5, 0),                # résultat nul
        (0, 0, 0),                # deux zéros
        (0, 7, -7),               # zéro en premier
        (7, 0, 7),                # zéro en second
        (-3, -8, 5),              # deux négatifs
        (-3, 8, -11),             # premier négatif
        (3, -8, 11),              # second négatif
        (1_000_000, 1, 999_999),  # grand nombre
    ],
)
def test_soustraction_valeurs(a, b, expected):
    response = client.get("/soustraction", params={"a": a, "b": b})
    assert response.status_code == 200
    assert response.json()["result a-b="] == expected


def test_soustraction_non_commutative():
    """a - b est different de b - a (sauf si a == b)."""
    r1 = client.get("/soustraction", params={"a": 9, "b": 2}).json()
    r2 = client.get("/soustraction", params={"a": 2, "b": 9}).json()
    assert r1["result a-b="] == 7
    assert r2["result a-b="] == -7


def test_soustraction_champ_developer():
    """Le champ developer est present (sa valeur n'est pas figee)."""
    response = client.get("/soustraction", params={"a": 1, "b": 1})
    assert "developer" in response.json()


def test_soustraction_parametre_manquant():
    response = client.get("/soustraction", params={"a": 5})
    assert response.status_code == 422


def test_soustraction_parametre_invalide():
    response = client.get("/soustraction", params={"a": "abc", "b": 2})
    assert response.status_code == 422


def test_soustraction_decimal_refuse():
    """Les parametres sont des int : 2.5 est refuse."""
    response = client.get("/soustraction", params={"a": 2.5, "b": 1})
    assert response.status_code == 422


def test_addition_non_regression():
    """Verifie que l'endpoint du TP2 fonctionne toujours."""
    response = client.get("/addition", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json()["result a+b="] == 8


def test_racine():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}