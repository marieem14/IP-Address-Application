# IP-Address-Application

# IP Address Application

## 1. Présentation du projet

**IP Address Application** est un projet réalisé dans le cadre du cours Cisco.

L'objectif est de développer une application en Python permettant de récupérer et d'afficher les informations relatives à l'adresse IP publique de l'utilisateur.

L'application vise à prendre en charge les deux versions du protocole IP : IPv4 et IPv6.

## 2. Objectifs du projet

Les principaux objectifs sont :

- Récupérer l'adresse IPv4 publique.
- Récupérer l'adresse IPv6 publique lorsqu'elle est disponible.
- Vérifier la validité des adresses IP.
- Obtenir des informations géographiques associées à une adresse IP.
- Afficher les informations récupérées dans une application Python.
- Utiliser la programmation orientée objet (POO).
- Communiquer avec des API REST et traiter les données JSON.

## 3. Technologies utilisées

| Technologie   | Utilisation                                |
| ------------- | ------------------------------------------ |
| Python        | Langage de programmation                   |
| POO           | Organisation du programme avec des classes |
| Requests      | Communication avec les API REST            |
| JSON          | Échange et traitement des données          |
| ipaddress     | Validation des adresses IPv4 et IPv6       |
| Pytest        | Tests unitaires                            |
| Git et GitHub | Gestion du code et collaboration           |

## 4. APIs utilisées

Le projet utilise des services externes pour récupérer les informations IP.

- **ipify** : service utilisé pour récupérer les adresses IP publiques.
- **IP-API** : service utilisé pour obtenir des informations de géolocalisation associées à une adresse IP, comme le pays, la ville et le fournisseur Internet (ISP).

Exemple d'endpoint utilisé pour la géolocalisation :

`http://ip-api.com/json/{ip}`

## 5. Structure du projet

```text
IP-Address-Application/
│
├── models/
│   └── ip_address.py
│
├── services/
│   └── api_client.py
│
├── application/
│   └── ip_application.py
│
├── utils/
│   └── ip_validator.py
│
├── tests/
│   └── test_api_client.py
│
├── main.py
├── requirements.txt
└── README.md
```

## 6. Travail réalisé jusqu'à présent

Le développement du projet est organisé en plusieurs parties.

### Partie 1 : Initialisation du projet

- Création du dépôt GitHub.
- Organisation initiale des fichiers et des dossiers.
- Configuration de l'environnement de travail.
- Mise en place du travail collaboratif avec Git et GitHub.

### Partie 2 : Développement du client API

Cette partie a été réalisée par le deuxième membre du groupe.

Le fichier `services/api_client.py` contient la classe `APIClient`, chargée de communiquer avec les services externes.

Le travail réalisé comprend :

- L'utilisation de la bibliothèque `requests`.
- La récupération des informations relatives aux adresses IP.
- La récupération des informations de géolocalisation.
- La validation d'une adresse IP avant de demander ses informations.
- La gestion des erreurs liées aux requêtes HTTP.

Une validation supplémentaire a été intégrée avec le module Python `ipaddress`.

### Partie 3 : Tests

Des tests unitaires ont été ajoutés avec `pytest` afin de vérifier le fonctionnement du client API et de la validation des adresses IP.

## 7. Travail restant

Les prochaines étapes du projet sont :

- Développer la classe `IPAddress` et ses attributs.
- Finaliser le module de validation des adresses IP.
- Développer la partie principale de l'application.
- Intégrer les différentes parties développées par les membres.
- Tester le fonctionnement global de l'application.
- Finaliser la documentation du projet.

## 8. Installation et exécution

### Prérequis

- Python 3 installé.
- Git installé.
- Visual Studio Code recommandé.

### Installation

Cloner le dépôt GitHub :

```bash
git clone URL_DU_DEPOT
```

Accéder au dossier du projet :

```bash
cd IP-Address-Application
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Pour exécuter les tests :

```bash
pip install pytest
pytest
```

L'exécution principale de l'application sera disponible après l'intégration de tous les modules.

## 9. Travail collaboratif

Le projet est réalisé par une équipe de trois membres.

- **Membre 1 :** Programmation Orientée Objet et gestion des adresses IP.
- **Membre 2 :** Communication avec les API REST et récupération des informations.
- **Membre 3 :** Scrum Leader, organisation du projet, intégration des modules et documentation.

La collaboration est assurée par Git et GitHub, avec des branches séparées et des Pull Requests pour intégrer les modifications dans la branche principale `main`.

## 10. Conclusion

Ce projet permet de mettre en pratique les connaissances en Python, en programmation orientée objet, en réseaux informatiques et en communication avec les API REST.

Il permet également de développer les compétences en travail collaboratif et en gestion de versions avec Git et GitHub.
