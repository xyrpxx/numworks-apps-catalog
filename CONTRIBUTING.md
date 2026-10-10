# Contribuer

Les contributions qui ajoutent une application vérifiable, corrigent une fiche ou recensent une source utile sont bienvenues.

## Ajouter un NWA à `catalog.json`

1. Choisir un lien amont HTTPS versionné : release stable, tag immuable ou commit précis.
2. Vérifier que le fichier cible est bien un `.nwa` et qu’il est publiquement téléchargeable.
3. Fournir un SHA-256 de 64 caractères hexadécimaux minuscules. Utiliser de préférence l’empreinte publiée par la release GitHub ou un fichier de sommes amont; si nécessaire, recalculer le fichier téléchargé avec `Get-FileHash -Algorithm SHA256` ou `sha256sum`.
4. Garder un `id` stable et unique. Ne jamais réutiliser un identifiant supprimé pour un autre logiciel.
5. Décrire honnêtement `requiresData`. Ajouter une note claire quand le logiciel a besoin d’un fichier de données, d’un ROM légalement obtenu, d’un firmware particulier ou d’une installation seule.
6. Séparer la licence du dépôt amont des droits des contenus tiers (marques, illustrations, musiques, polices).
7. Distinguer compatibilité annoncée par l’auteur et tests réellement effectués. Ne jamais présenter une annonce amont comme une validation matérielle du présent catalogue.

Le dépôt de NumWorks Manager accepte une empreinte dans le catalogue et vérifie celle du téléchargement avant import. Les champs supplémentaires sont ignorés par le lecteur v1 actuel; documentez donc les contraintes importantes dans `description`.

Si un NWA n’a pas d’empreinte fiable, de lien amont stable ou de provenance assez claire, ajoutez plutôt une fiche dans `directory.json` avec `status` explicite, ou attendez de pouvoir vérifier les informations. Ne copiez pas les NWA dans ce dépôt.

## Ajouter un script, un thème ou un projet à `directory.json`

- Choisir `kind` et `status` qui décrivent exactement le format et le mode d’installation.
- Ajouter au moins un lien amont HTTPS maintenu.
- Préciser le modèle/firmware nécessaire lorsque la source le documente.
- Pour un script Python, signaler qu’il ne s’agit pas d’un NWA.
- Pour un thème, ne pas le présenter comme installable sur Epsilon si son amont demande Omega/Upsilon ou une compilation du firmware.
- Ajouter une courte note de licence sans attribuer au dépôt central les droits amont.

## Vérification locale

```powershell
python scripts/validate_catalog.py
```

Le script vérifie les champs obligatoires du lecteur v1, les identifiants, les URL HTTPS, les sommes SHA-256 et les références entre annuaire et catalogue. Il ne télécharge pas les NWA et ne valide pas le fonctionnement sur calculatrice.
