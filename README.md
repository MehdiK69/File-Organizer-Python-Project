# FileOrganizer

Script Python qui organise automatiquement les fichiers d'un dossier par catégorie.

## Fonctionnement

Le script scanne un dossier `sandbox/` et déplace les fichiers dans des sous-dossiers
créés automatiquement selon leur extension :

| Catégorie  | Extensions              |
| ---------- | ----------------------- |
| images/    | .jpg, .jpeg, .png, .gif |
| documents/ | .pdf, .docx, .txt, .md  |
| videos/    | .mp4, .mov, .avi        |
| autres/    | tout le reste           |

## Stack technique

- **Langage** : Python 3
- **Librairie** : pathlib (standard)

## Utilisation

```bash
python main.py
```

> Les fichiers du dossier `sandbox/` seront automatiquement triés.

## Fonctionnalités

- [x] Tri automatique par extension
- [x] Création automatique des sous-dossiers
- [x] Compteur de fichiers par catégorie
- [ ] Support d'autres extensions (en cours)
- [ ] Interface en ligne de commande (à venir)

## Fichiers ignorés

Le dossier `sandbox/` contient les fichiers de test et n'est pas inclus dans le dépôt.
