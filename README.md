# IP Address Application

## 1. Présentation du projet

IP Address Application est un projet réalisé dans le cadre du cours de réseaux informatiques et du programme Cisco.

L'objectif est de développer une application en Python permettant de récupérer et d'afficher les informations relatives à l'adresse IP publique de l'utilisateur.

L'application prend en considération les deux versions du protocole Internet : IPv4 et IPv6.

## 2. Objectifs du projet

Les principaux objectifs sont :

- Récupérer l'adresse IPv4 publique.
- Récupérer l'adresse IPv6 publique lorsqu'elle est disponible.
- Vérifier la validité des adresses IP.
- Obtenir des informations géographiques associées à une adresse IP.
- Afficher les informations récupérées dans une application Python.
- Utiliser la programmation orientée objet (POO).
- Communiquer avec des API REST et traiter les données JSON.
- Appliquer les principes du travail collaboratif avec Git et GitHub.

## 3. Technologies et outils utilisés

| Technologie        | Utilisation                                |
| ------------------ | ------------------------------------------ |
| Python             | Développement de l'application             |
| POO                | Organisation du programme avec des classes |
| Requests           | Communication avec les API REST            |
| JSON               | Traitement des réponses des API            |
| ipaddress          | Validation des adresses IP                 |
| Pytest             | Exécution des tests                        |
| Git                | Gestion des versions                       |
| GitHub             | Hébergement et collaboration               |
| Visual Studio Code | Environnement de développement             |

## 4. APIs utilisées

Le projet utilise des services externes pour récupérer les informations IP.

- **ipify** : récupération des adresses IP publiques IPv4 et IPv6.
- **IP-API** : récupération des informations de géolocalisation associées à une adresse IP, notamment le pays, la ville et le fournisseur Internet (ISP).

Les informations dépendent de la disponibilité des services API et de la connexion Internet.

## 5. Structure du projet

```text
IP-Address-Application/
│
├── models/
│   ├── __init__.py
│   └── ip_address.py
│
├── services/
│   ├── __init__.py
│   └── api_client.py
│
├── application/
│   ├── __init__.py
│   └── ip_application.py
│
├── utils/
│   ├── __init__.py
│   └── ip_validator.py
│
├── tests/
│   ├── test_api_client.py
│   ├── test_ip_address.py
│   └── test_ip_validator.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Organisation du travail

Le projet est réalisé par une équipe de trois membres :

- **Membre 1 :** développement de la classe IPAddress et des fonctions de validation des adresses IP.
- **Membre 2 :** développement du client API pour récupérer les adresses IP et les informations de géolocalisation.
- **Membre 3 :** Scrum Leader, organisation du dépôt GitHub, documentation, suivi des contributions et intégration des différents modules.

Chaque membre travaille sur sa partie et les modifications sont regroupées dans la branche principale après vérification.

## 7. Travail réalisé

Les premières étapes du projet comprennent :

- La création et l'organisation du dépôt GitHub.
- La mise en place de l'accès collaboratif pour les membres.
- Le clonage du dépôt dans l'environnement local.
- La préparation de la structure du projet.
- Le développement des modules de gestion des adresses IP et de communication avec les API.
- La création des premiers tests.
- La mise à jour de la documentation du projet.
- La préparation du fichier des dépendances Python.

## 8. Installation des dépendances

### Prérequis

- Python 3 installé.
- Git installé.
- Visual Studio Code recommandé.

### Clonage du dépôt

```bash
git clone URL_DU_DEPOT
```

Accéder au dossier :

```bash
cd IP-Address-Application
```

### Installation des bibliothèques

```bash
python -m pip install -r requirements.txt
```

## 9. Exécution et tests

Après l'intégration de tous les modules, l'application pourra être lancée avec :

```bash
python main.py
```

Pour exécuter les tests :

```bash
python -m pytest -v
```

## 10. Travail restant

Les étapes à finaliser sont :

- Vérifier la compatibilité entre les différents modules.
- Finaliser l'intégration de la classe IPAddress et du client API.
- Finaliser le programme principal.
- Tester le fonctionnement global de l'application.
- Corriger les erreurs éventuelles.
- Vérifier la documentation et préparer la démonstration finale.

## 11. Conclusion

Ce projet permet de mettre en pratique les connaissances en Python, en programmation orientée objet, en réseaux informatiques et en communication avec les API REST.

Il permet également de développer les compétences en gestion de versions, en collaboration et en organisation d'un projet informatique.
