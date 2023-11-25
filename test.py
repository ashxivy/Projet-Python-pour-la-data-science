import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Charger le fichier CSV
file_path = 'data\openfoodfacts.csv'
# Charger le fichier CSV dans un DataFrame pandas
df = pd.read_csv(file_path, sep='\t',low_memory=True)  # Assurez-vous de spécifier le bon séparateur s'il est différent de la virgule

# Afficher les premières lignes du DataFrame pour voir les données
<<<<<<< HEAD
print(df.head())

#On vérifie que la base est bien chargée

df.sample(5)
print ("Le dataset compte {} lignes et {} variables".format(df.shape[0], df.shape[1]))

# Afficher les noms des colonnes du DataFrame
print(df.columns)

#on veut connaître les valeurs de la colonne countries_fr
valeurs_uniques = df['countries_fr'].unique()
print(valeurs_uniques)

valeurs_uniques_tag = df['countries_tags'].unique()
print(valeurs_uniques_tag)

=======
print(df.head())
>>>>>>> parent of e5c30cf (on lance le projet)
