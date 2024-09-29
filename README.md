# ServicesWindowsPython

Ce projet contient un service Windows écrit en Python pour la gestion de caméra. 
cela ma permit de tester la gestion des services windows en python.
Le service exécute un script Python qui écrit "Hello World" dans un fichier toutes les minutes.

## Prérequis

- Python 3.9 ou supérieur
- `pywin32` pour les services Windows

## Installation

### 1. Installer Python

Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).

### 2. Installer les dépendances

Installez `pywin32` en utilisant pip :
pip install pywin32



## Installation du service Windows

Pour installer le service, exécutez la commande suivante dans le terminal :
python script_service.py install

## Désinstaller le service

Pour désinstaller le service, exécutez la commande suivante :
python script_service.py remove


## Journaux

Les journaux du service sont écrits dans `C:\python\service_log.txt`. Le script `test.py` écrit ses journaux dans `C:\python\test_log.txt` et ses sorties dans `C:\python\output.txt`.

## Auteurs

- [franck51000](https://github.com/franck51000)

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
