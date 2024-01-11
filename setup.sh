#!/bin/bash

# Créer un environnement virtuel
python3 -m venv env

# Activer l'environnement virtuel
source env/bin/activate

# Installer les dépendances
pip install -r requirements.txt

echo "L'environnement virtuel est configuré et les dépendances sont installées."
