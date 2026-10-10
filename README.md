# NumWorks Apps Catalog

Catalogue communautaire pour alimenter la bibliothèque de **NumWorks Manager** et retrouver les projets utiles de l’écosystème NumWorks.

> Les fichiers NWA ne sont pas copiés ici. Le catalogue pointe vers les sources amont versionnées et publie leur SHA-256. Les scripts, thèmes et projets qui ne rentrent pas dans le flux NWA sont recensés dans l’annuaire.

## Ajouter le catalogue dans NumWorks Manager

Dans **Sources**, ajoute cette URL HTTPS puis actualise la source :

```text
https://raw.githubusercontent.com/xyrpxx/numworks-apps-catalog/main/catalog.json
```

Le fichier utilise le format catalogue v1 de NumWorks Manager : `schemaVersion: 1` et `applications[]`. Chaque entrée fournit `id`, `name`, `description`, `version`, `downloadUrl`, `sha256` et `requiresData`.

L’application importe seulement les NWA choisis. Les champs additionnels (catégorie, compatibilité, licence et provenance) sont conservés pour les lecteurs futurs, mais l’écran Sources actuel n’affiche pas encore une fiche complète de ces métadonnées.

## Contenu initial

- **26 NWA NumPlay v1.7.5** : bundle, jeux individuels et variantes Epsilon. Les trois gros jeux que l’amont signale comme autonomes sont annotés `standaloneOnly`.
- **Multi-Cheatsheet NumWorks 2.2.2** : nécessite `gallery.bin`, exporté séparément depuis l’éditeur amont.
- **NumPlay-Upsilon** est dans `directory.json`, pas dans le flux installable standard : le mainteneur le destine à Upsilon sur N0110/N0115 et indique une installation par `nwlink`.
- **Annuaire** : [directory.json](directory.json) répertorie aussi les bibliothèques Python, collections communautaires, projets et thèmes.

Ce premier jeu de données n’est **pas encore exhaustif**. Il privilégie les NWA pour lesquels une version amont stable et un SHA-256 publiquement vérifiable sont disponibles. Pour les applications de Nwagyu, NumWorks Manager peut également découvrir directement les fichiers NWA en ajoutant le dépôt GitHub public comme source; elles ne sont pas déclarées ici avec une empreinte que nous n’avons pas vérifiée.

## Provenance, compatibilité et droits

- NumPlay est publié sous GPL-3.0 au niveau du dépôt. Son README précise que les noms, illustrations et musiques issus des jeux tiers restent à leurs titulaires et ne sont pas couverts par la licence du dépôt.
- Multi-Cheatsheet est publié sous GPL-3.0. Sa somme SHA-256 provient de son fichier amont `SHA256SUMS.txt`.
- Pour NumPlay, les modèles et versions Epsilon sont des déclarations du README amont, pas des tests matériels de ce dépôt. Les entrées marquées `standaloneOnly` doivent être interprétées selon les notes de l’auteur.
- Les liens et les empreintes identifient des fichiers amont; ils ne changent pas leurs licences et ne signifient pas que ce dépôt héberge ou possède ces logiciels.
- Les fiches Python, les thèmes Omega/Upsilon et les projets de firmware ne sont pas des NWA importables par cette URL; consultez l’annuaire pour leurs consignes propres.

Les métadonnées originales de ce dépôt sont sous MIT. Cette licence ne s’applique pas aux logiciels, marques, textes, images ou musiques liés.

## Fichiers

| Fichier | Rôle |
|---|---|
| `catalog.json` | Flux JSON importable par NumWorks Manager |
| `directory.json` | Annuaire informatif, non consommé comme catalogue d’installation |
| `schemas/catalog.schema.json` | Schéma de validation du flux installable |
| `schemas/directory.schema.json` | Schéma de validation de l’annuaire |
| `scripts/validate_catalog.py` | Validation locale avec la bibliothèque standard Python |
| `CONTRIBUTING.md` | Règles d’ajout et de mise à jour |

## Valider les fichiers

Depuis la racine du dépôt :

```powershell
python scripts/validate_catalog.py
```

## English

A community catalog for NumWorks Manager. It links to upstream, versioned NWA files and records SHA-256 digests without mirroring the binaries. Non-NWA scripts, themes and projects are listed separately in `directory.json`. The initial dataset is curated, not exhaustive.
