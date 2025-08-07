# 🚀 Release Announcer

Automatisierter GitHub → X (Twitter) Release-Poster.  
Dieses Projekt überwacht neue Releases in einem GitHub-Account oder einer Organisation und postet diese automatisch zu **X** – wahlweise im **Debug-/Testmodus**.

---

## 📦 Version
**0.9.9 (Unreleased)**

---

## ✨ Features
- Überwacht alle Repos eines Accounts oder einer Organisation
- Erkennt neue Releases über die GitHub API
- Postet automatisch einen Ankündigungstext zu X (Twitter)
- **Debug-/Testmodus** zum gefahrlosen Testen ohne Live-Posting
- GitHub Actions Workflow inklusive

---

## 🧪 Sicher testen (Debug-Modus)
Um sicherzustellen, dass beim Testen **keine Live-Posts an X gesendet werden**, kann der Debugmodus aktiviert werden:

1. Öffne im Repo **Settings → Secrets and variables → Actions → New repository secret**
2. Erstelle ein Secret:
   - **Name:** `DEBUG_MODE`  
   - **Value:** `true` (klein geschrieben, ohne Anführungszeichen)
3. Speichern.

🔹 **Deaktivieren**: Secret `DEBUG_MODE` löschen oder Wert auf `false` setzen.

---

## ⚙️ Voraussetzungen
- Python 3.8+ installiert
- GitHub Personal Access Token (nur Lesezugriff erforderlich)
- X (Twitter) API Key & Access Token

---

## 🔑 Benötigte GitHub Secrets
| Name              | Beschreibung |
|-------------------|--------------|
| `GH_TOKEN`        | GitHub Personal Access Token (Repo Read) |
| `X_API_KEY`       | API Key von X (Twitter Developer Portal) |
| `X_API_SECRET`    | API Secret von X |
| `X_ACCESS_TOKEN`  | Access Token von X |
| `X_ACCESS_SECRET` | Access Secret von X |
| `DEBUG_MODE`      | `true` = Testmodus, `false` = Live-Posting |

---

## 📜 Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](./LICENSE.md).  
Frei verwendbar – auch für eigene Projekte & Schulungsunterlagen.

---

## 🧾 Changelog
Alle Änderungen werden im [CHANGELOG.md](./CHANGELOG.md) dokumentiert.

---

© 2025 André Hohenstein – Microsoft Certified Trainer
