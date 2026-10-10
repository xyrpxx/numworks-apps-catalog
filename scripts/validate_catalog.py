#!/usr/bin/env python3
"""Validate the installable NumWorks catalog and its informational directory."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
DIRECTORY = ROOT / "directory.json"
ID_RE = re.compile(r"^[A-Za-z0-9_.-]{1,100}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def fail(message: str) -> None:
    raise SystemExit(f"ERREUR: {message}")


def https_url(value: object, label: str, allow_fragment: bool = False) -> None:
    if not isinstance(value, str):
        fail(f"{label}: URL absente ou non textuelle")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password or (parsed.fragment and not allow_fragment):
        fail(f"{label}: URL HTTPS invalide: {value}")


catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
if catalog.get("schemaVersion") != 1 or not isinstance(catalog.get("applications"), list):
    fail("catalog.json doit avoir schemaVersion=1 et applications[]")

ids: set[str] = set()
for index, app in enumerate(catalog["applications"]):
    where = f"catalog.json applications[{index}]"
    if not isinstance(app, dict):
        fail(f"{where}: objet attendu")
    for key in ("id", "name", "description", "version", "downloadUrl", "sha256", "requiresData"):
        if key not in app:
            fail(f"{where}: champ requis manquant: {key}")
    app_id = app["id"]
    if not isinstance(app_id, str) or not ID_RE.fullmatch(app_id) or app_id in ids:
        fail(f"{where}: id invalide ou dupliqué: {app_id!r}")
    ids.add(app_id)
    if not isinstance(app["name"], str) or not app["name"] or len(app["name"]) > 160:
        fail(f"{where}: name invalide")
    if not isinstance(app["description"], str) or len(app["description"]) > 4000:
        fail(f"{where}: description invalide")
    if not isinstance(app["version"], str) or not app["version"] or len(app["version"]) > 160:
        fail(f"{where}: version invalide")
    if not isinstance(app["requiresData"], bool):
        fail(f"{where}: requiresData doit être booléen")
    if not isinstance(app["sha256"], str) or not SHA256_RE.fullmatch(app["sha256"]):
        fail(f"{where}: SHA-256 invalide")
    https_url(app["downloadUrl"], f"{where}.downloadUrl")
    if not urlparse(app["downloadUrl"]).path.lower().endswith(".nwa"):
        fail(f"{where}: downloadUrl ne pointe pas vers un .nwa")
    if "iconUrl" in app:
        https_url(app["iconUrl"], f"{where}.iconUrl")

directory = json.loads(DIRECTORY.read_text(encoding="utf-8"))
if directory.get("directoryVersion") != 1 or not isinstance(directory.get("items"), list):
    fail("directory.json doit avoir directoryVersion=1 et items[]")
directory_ids: set[str] = set()
for index, item in enumerate(directory["items"]):
    where = f"directory.json items[{index}]"
    if not isinstance(item, dict):
        fail(f"{where}: objet attendu")
    for key in ("id", "name", "kind", "description", "urls", "status"):
        if key not in item:
            fail(f"{where}: champ requis manquant: {key}")
    if not isinstance(item["id"], str) or item["id"] in directory_ids:
        fail(f"{where}: id invalide ou dupliqué")
    directory_ids.add(item["id"])
    if not isinstance(item["urls"], list) or not item["urls"]:
        fail(f"{where}: urls doit être une liste non vide")
    for link_index, link in enumerate(item["urls"]):
        if not isinstance(link, dict) or not isinstance(link.get("label"), str):
            fail(f"{where}.urls[{link_index}]: lien invalide")
        https_url(link.get("url"), f"{where}.urls[{link_index}].url", allow_fragment=True)
    for related_id in item.get("relatedCatalogIds", []):
        if related_id not in ids:
            fail(f"{where}: identifiant catalogue inconnu: {related_id}")

print(f"OK: {len(ids)} applications NWA et {len(directory_ids)} entrées informatives.")
