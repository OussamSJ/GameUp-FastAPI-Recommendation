#Déscription du projet :

##Ce projet est une API RESTful développée avec FastAPI pour  recevoire les données des utilisateurs et leurs achats de jeux vidéo et renvoyer des recommandations de jeux basées sur les données reçues.


#Installation des dépendances nécessaires pour le projet :

##pip install fastapi uvicorn

##pip install pydantic

##pour lancer le projet  :  uvicorn main:app --reload


#Commentaires :
 
##Il est tout à fait possible de modifier le model UserData pour inclure d'autres champs 
si nécessaire, par exemple des paramètres supplémentaires sur l'utilisateur ou le jeu. 
 class UserData(BaseModel):
    #user_id: int
    #game_id: int
    #rating: float
    #purchase : bool
    #wishlist: bool
    #quantite: int 

##Le modèle pourrait utiliser ces champs pour construire une note pondérée et générer la recommandation.