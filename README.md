# Classification et Détection avec SVM et Réseau de Neurones

## Introduction
Ce projet implémente deux approches de Machine Learning et Deep Learning pour la classification et la détection d'attaques.

1. **Support Vector Machine (SVM)** : Utilisé pour la classification binaire, permettant de distinguer les attaques des comportements normaux.
2. **Neural Network (NN)** : Un réseau de neurones conçu pour classifier le type exact d'attaque après la détection initiale.

Ce projet suit un pipeline structuré incluant le chargement des données, le prétraitement, l'entraînement des modèles et l'évaluation des performances.

## 1. Installation et Configuration
Avant d'exécuter le projet, il est recommandé d'utiliser un environnement virtuel Python pour isoler les dépendances.

### Étape 1 : Création d'un environnement virtuel
```bash
python -m venv venv
```

### Étape 2 : Activation de l'environnement virtuel
- **Windows (CMD/Powershell)**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**
  ```bash
  source venv/bin/activate
  ```

### Étape 3 : Installation des dépendances
```bash
pip install -r requirements.txt
```

## 2. Explication des Processus

### 2.1. Chargement et Prétraitement des Données
Les données utilisées pour l'entraînement des modèles sont chargées à partir de la fusion de 2 fichiers CSV ou d'une base de données. Les étapes de prétraitement incluent :
- Nettoyage des données
- Transformation des variables catégoriques
- Normalisation des valeurs numériques
- Séparation en ensembles d'entraînement et de test

### 2.2. Classification Binaire avec SVM
L'algorithme **Support Vector Machine (SVM)** est une méthode de Machine Learning utilisée pour séparer les données en deux classes distinctes (attaque vs normal).

**Étapes de l'entraînement SVM :**
1. Séparation des données en features (X) et labels (y)
2. Utilisation d'un SVM avec un noyau Radial Basis Function (rbf)
3. Optimisation des hyperparamètres via validation croisée
4. Entraînement du modèle sur l'ensemble d'entraînement
5. Évaluation sur l'ensemble de test

#### 2.2.1 Noyau RBF
Utilisation :
Fonctionne bien lorsque les frontières de séparation ne sont pas linéaires.
Très efficace pour des données complexes et non linéaires.
Inconvénient :
Peut être difficile à optimiser.

### 2.3. Classification Multi-Classes avec Réseau de Neurones (NN)
Une fois qu'une attaque est détectée par le SVM, un **réseau de neurones** est utilisé pour classifier le type exact d'attaque.

**Architecture du Réseau de Neurones :**
- Plusieurs couches denses (Fully Connected Layers)
- Fonction d'activation ReLU
- Couches de dropout pour éviter l'overfitting
- Fonction softmax en sortie pour classifier les types d'attaques

L'entraînement du réseau de neurones suit ces étapes :
1. Transformation des labels en format one-hot encoding
2. Entraînement avec descente de gradient (Adam optimizer)
3. Évaluation sur l'ensemble de test avec métriques de performance

### 2.4. Évaluation et Visualisation
Les modèles sont évalués à l'aide de plusieurs métriques :
- **Accuracy** : Précision globale de la classification
- **Precision, Recall, F1-Score** : Performance pour chaque classe
- **Matrice de confusion** : Visualisation des erreurs de classification

## 3. Conclusion
Ce code met en œuvre une approche hybride combinant **SVM** (ML) pour la classification binaire et **NN** (DL) pour l'identification des types d'attaques. Cette méthodologie permet une analyse approfondie des données de sécurité et peut être adaptée à d'autres domaines nécessitant une détection automatique avancée.

