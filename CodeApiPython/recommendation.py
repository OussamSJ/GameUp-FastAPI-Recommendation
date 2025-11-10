import pandas as pd
import joblib
from models import UserData
from data_loader import load_training_data
from sklearn.neighbors import NearestNeighbors


# Chargement du modèle et des données à l’importation
model_knn = joblib.load("data/knn_model.joblib")
user_game_matrix = pd.read_pickle("data/user_game_matrix.pkl")
data =  load_training_data("data/ratings_data.csv")             

def generate_recommendations(user_data: UserData, top_n=3):
    temp_matrix = user_game_matrix.copy()

     # Vérifier que le jeu demandé existe bien dans le modèle
    if user_data.game_id not in user_game_matrix.columns:
        # Données d'exemple par défaut
        return [
            {"game_id": 101, "game_name": "Pandemic"},
            {"game_id": 102, "game_name": "Catan"},
            {"game_id": 103, "game_name": "Ticket to Ride"},
        ]

    # Ajouter l'utilisateur si non présent
    if user_data.user_id not in temp_matrix.index:
        temp_matrix.loc[user_data.user_id] = 0
    temp_matrix.loc[user_data.user_id, user_data.game_id] = user_data.rating

    # Trouver les utilisateurs similaires
    distances, indices = model_knn.kneighbors(temp_matrix.loc[[user_data.user_id]], n_neighbors=4)
    similar_users = temp_matrix.index[indices.flatten()[1:]]

    # Extraire leurs notes
    similar_data = data[data['user_id'].isin(similar_users)]

    # Moyenne des notes des utilisateurs similaires
    avg_scores = (
        similar_data.groupby(["game_id", "game_name"])["note"]
        .mean()
        .sort_values(ascending=False)
    ).reset_index()

    # Exclure les jeux déjà notés
    already_rated = set(temp_matrix.loc[user_data.user_id][temp_matrix.loc[user_data.user_id] > 0].index)

    # Générer la recommandation
    recommendations = [
        {"game_id": row["game_id"], "game_name": row["game_name"]}
        for _, row in avg_scores.iterrows()
        if row["game_id"] not in already_rated
    ][:top_n]

    return recommendations






