# Détection d'attaques via Machine Learning et Deep Learning

Ce projet implémente un pipeline de détection d'attaques réseau en utilisant des modèles de **Machine Learning (ML)** et **Deep Learning (DL)**.

## Données utilisées

Les données proviennent de :

- **Friday-WorkingHours-Afternoon-DDos.pcap\_ISCX.csv**
- **2023-02-12.csv**

Les jeux de données sont nettoyés, normalisés et transformés pour s'assurer de leur compatibilité avant d'être utilisés pour l'entraînement des modèles.

## Prérequis

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


## Classification et Détection avec Decision Tree et réseau de neurones artificiel 

Il s'appuie sur des ensembles de données de trafic réseau, les prétraite, effectue un rééquilibrage des classes, puis entraîne :

- Un **Decision Tree Classifier** pour la classification binaire (benin vs attaque).
- Un **réseau de neurones artificiel (ANN)** pour une classification plus fine des types d'attaques.

### 1. **Prétraitement des données**

- Chargement et harmonisation des noms de colonnes.
- Sélection des colonnes communes aux deux datasets.
- Fusion et nettoyage des données.
- Remplacement des valeurs infinies et suppression des valeurs manquantes.
- Création des labels :
  - `label_ml` : 1 si attaque, 0 sinon.
  - `label_dl` : Classification multi-classe des attaques.

### 2. **Modèle Machine Learning (Decision Tree)**

- Standardisation des features.
- Séparation des données en ensemble d'entraînement et de test.
- Optimisation des hyperparamètres via :
  - **RandomizedSearchCV**
  - **Optuna**
- Sélection des meilleurs hyperparamètres.
- Entraînement du **Decision Tree Classifier**.
- Prédictions et ajout des résultats dans les données.

### 3. **Rééquilibrage des données (SMOTE + Under-Sampling)**

- Utilisation de **SMOTE** pour augmenter les classes minoritaires.
- Réduction de la classe majoritaire via **RandomUnderSampler**.
- Transformation des labels en encodage one-hot pour le modèle DL.

### 4. **Modèle Deep Learning (ANN)**

- Construction d'un réseau de neurones avec plusieurs couches denses (relu + softmax en sortie).
- Optimisation de l'architecture via une grille de recherche.
- Entraînement du modèle avec **Adam optimizer** et **cross-entropy loss**.
- Évaluation sur un ensemble de test.


### Résultats attendus

- **Modèle ML (Decision Tree)** : Détection efficace des attaques avec optimisation des hyperparamètres.
- **Modèle DL (ANN)** : Classification multi-classe plus précise après data augmentation.


## Classification et Détection avec SVM et Réseau de Neurones

1. **Support Vector Machine (SVM)** : Utilisé pour la classification binaire, permettant de distinguer les attaques des comportements normaux.
2. **Neural Network (NN)** : Un réseau de neurones conçu pour classifier le type exact d'attaque après la détection initiale.

Ce projet suit un pipeline structuré incluant le chargement des données, le prétraitement, l'entraînement des modèles et l'évaluation des performances.

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


## Classification et Détection avec Random Forest et CNN 1D

Ce projet implémente une approche hybride pour détecter et classifier les attaques réseau en deux étapes :

1. **Détection d'attaque avec Random Forest** : Identification si une entrée est un trafic normal ou une attaque.

2. **Détection d'attaque avec Random Forest** : Une fois une attaque détectée, un réseau de neurones convolutionnel (CNN) est utilisé pour identifier le type d'attaque.

### Explication des Processus

### Classification Binaire avec Random Forest

L'algorithme Random Forest (RF) est une méthode de Machine Learning basée sur un ensemble d'arbres de décision. Il permet de séparer les données en deux classes distinctes (attaque vs normal).

#### Étapes de l'entraînement Random Forest :

  1. Séparation dL'algorithme Random Forest (RF) est une méthode de Machine Learning basée sur un ensemble d'arbres detraînement du modèle sur l'ensemble d'entraînement

  2. Évaluation sur l'ensemble de test

### Classification Multi-Classes avec Réseau de Neurones Convolutionnel (CNN)

Une fois qu'une attaque est détectée par Random Forest, un réseau de neurones convolutionnel (CNN) est utilisé pour classifier le type exact d'attaque.

#### Architecture du CNN :

* Plusieurs couches de convolution pour extraire les caractéristiques

* Fonction d'activation ReLU

* Couches de pooling pour réduire la dimension

* Couches de dropout pour éviter l'overfitting

* Fonction softmax en sortie pour classifier les types d'attaques

#### L'entraînement du CNN suit ces étapes :

* Transformation des labels en format one-hot encoding

* Entraînement avec descente de gradient (Adam optimizer)

* Évaluation sur l'ensemble de test avec métriques de performance


## Auteur

Projet réalisé dans le cadre de l'analyse de sécurité réseau avec honeypots. 🚀
Réalisé par :
  - Allan GUILLARD
  - Othman IBRAHIMI
  - Childéric OLIET
Accompagné par :
  - Rebiha Souadih
