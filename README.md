# Première application Python avec FastAPI

## Lancement de l'application

Installer les dépendances :

python -m pip install fastapi uvicorn

Lancer le serveur :

python -m uvicorn main:app --reload

L'application est accessible à l'adresse suivante :

http://127.0.0.1:8000/

## Tester l'application

1. Démarrer le serveur avec la commande indiquée ci-dessus.
2. Ouvrir http://127.0.0.1:8000/ dans un navigateur.
3. Vérifier que la réponse JSON suivante est retournée :

{
  "message": "it works !"
}

4. Il est également possible de tester la route GET / depuis la documentation interactive :

http://127.0.0.1:8000/docs
127.0.0.1