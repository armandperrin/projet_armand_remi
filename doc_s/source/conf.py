# conf.py

import os
import sys

sys.path.insert(
    0, os.path.abspath("../modules")
)  # Ajoute le chemin vers le dossier contenant my_module.py

project = "My Project"
author = "Your Name"
release = "0.1"

extensions = [
    "sphinx.ext.autodoc",  # Pour l'auto-documentation
    "sphinx.ext.viewcode",  # Pour inclure le code source
]

html_static_path = ["_static"]  # Chemin vers les fichiers statiques

html_theme = "sphinx_material"

html_theme_options = {
    "nav_title": "My Project",  # Titre dans la navigation
    "color_primary": "indigo",  # Couleur principale
    "color_accent": "orange",  # Couleur d'accent
    "logo_icon": "fa fa-cog",  # Icône pour le logo
    "favicon": "path/to/favicon.ico",  # Chemin vers le favicon
    "base_url": "file:///C:/Users/Bachelor/Documents/code_source/build/html/index.html",  # Change ça avec l'URL de ton projet
    "globaltoc_depth": 2,  # Profondeur de la table des matières
    "globaltoc_collapse": True,  # Activer le repli de la table des matières
}
