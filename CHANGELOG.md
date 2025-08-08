# 📜 Changelog – Release Announcer

Alle relevanten Änderungen an diesem Projekt werden hier dokumentiert.  

---

## [1.0.0] – 2025-08-08
### Added
- Erste stabile Version – **Production Ready**
- Dokumentation des **Debug-/Testmodus** (`DEBUG_MODE` Secret) in README
- Hinweis zum Umschalten zwischen Test- und Produktivmodus
- Vollständige Anleitung zur Einrichtung der GitHub Secrets für X
- Workflow final getestet (Debug- und Livebetrieb)

### Changed
- README angepasst, Pre-Release-Hinweis entfernt
- CHANGELOG für v1.0.0 ergänzt

---

## [0.9.9] – 2025-08-07
### Added
- Dokumentation des **Debug-/Testmodus** (`DEBUG_MODE` Secret) in README
- Hinweis zum Umschalten zwischen Test und Live

### Changed
- README-Version auf 0.9.9 gesetzt

---

## [0.9.8] – 2025-08-07
### Added
- Initiale Projektstruktur erstellt
- `scan_releases.py` implementiert (GitHub API-Abfrage aller Repos & Orgs)
- `post_to_x.py` integriert (Twitter/X-Posting)
- GitHub Actions Workflow `announce-on-x.yml` erstellt
- `.gitignore`, `README.md` und `CHANGELOG.md` hinzugefügt
