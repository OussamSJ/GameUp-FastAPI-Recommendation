# 🧠 GameUP Recommendation API

## 📖 Description
Cette API Python, développée avec **FastAPI**, constitue le moteur de **recommandation intelligente** de la plateforme **GamesUP**.  
Elle analyse les données utilisateurs et leurs historiques d’achats afin de proposer des **recommandations personnalisées** de jeux vidéo.

Le modèle `UserData` peut être étendu pour inclure d’autres champs, par exemple :
```python
class UserData(BaseModel):
    # user_id: int
    # game_id: int
    # rating: float
    # purchase: bool
    # wishlist: bool
    # quantite: int
```

## ⚙️Objectifs du projet

Mettre en place un système de recommandation KNN.

Offrir une API REST consommée par l’API Spring Boot principale.

Gérer les échanges de données utilisateurs et de jeux.

Préparer l’infrastructure pour l’entraînement et l’évolution du modèle.

## 🧩 Architecture technique

Framework : FastAPI

Langage : Python 3.11+

Machine Learning : scikit-learn (modèle KNN)

Communication : REST JSON (avec l’API Spring Boot)


##📡 Endpoints principaux

| Méthode | Endpoint     | Description                                                               |
| ------- | ------------ | ------------------------------------------------------------------------- |
| `POST`  | `/recommendations` | Renvoie les recommandations de jeux pour un utilisateur donné             |
| `GET`   | `/`    | Vérifie le statut de l’API                                                |

## 🧠 Algorithme utilisé

L’algorithme K-Nearest Neighbors (KNN) est utilisé pour identifier les jeux similaires à ceux achetés ou aimés par un utilisateur.
Les données manipulées incluent :

Identifiant du jeu

Identifiant d'utilisateur

Catégorie / éditeur / auteur

Historique de notes utilisateur

Le modèle peut être étendu pour inclure des informations supplémentaires sur l’utilisateur ou le jeu afin d’améliorer les recommandations.

## 🚀 Lancer le projet localement
### Prérequis

Python 3.11+

pip

### Installation des dépendances
```
pip install fastapi uvicorn
pip install pydantic
```

### Lancement du projet
```
uvicorn main:app --reload
```

