from pydantic import BaseModel
from typing import List



class UserData(BaseModel):
    user_id: int
    game_id: int
    rating: float
    

#Il est tout à fait possible de modifier le model UserData pour inclure d'autres champs 
#si nécessaire, par exemple pour des paramètres supplémentaires sur l'utilisateur ou le jeu. 

#class UserData(BaseModel):
    #user_id: int
    #game_id: int
    #rating: float
    #purchase : bool
    #wishlist: bool
    #quantite: int 

#Le modèle pourrait utiliser des champs supplémentaires comme `purchase` ou `wishlist` pour 
#construire une note pondérée et générer la recommandation.