# 📢 Release Announcer – GitHub Releases → X (Twitter) Auto-Poster

> **Version:** 1.0 – 2025-08-07  

---

## 🎯 Ziel
Dieses Projekt überwacht **alle Repositories** eines GitHub-Users (und optional Organisationen) und postet automatisch einen Tweet auf **X (Twitter)**, sobald ein neues Release erscheint.  
Die Lösung ist **zentral** – es muss **nichts** in den Quell-Repos geändert werden.

---

## 📂 Projektstruktur
```
.github/
└─ workflows/
   └─ announce-on-x.yml   # GitHub Actions Workflow
src/
├─ scan_releases.py       # Scannt Repos und erkennt neue Releases
└─ post_to_x.py           # Postet Release-Infos auf X
state/
├─ known_releases.json    # Bereits gepostete Releases (ID-Tracking)
└─ pending.json           # Noch nicht gepostete Releases
requirements.txt          # Python-Abhängigkeiten
README.md                 # Diese Datei
CHANGELOG.md              # Änderungsprotokoll
```

---

## 🛠 Voraussetzungen
- GitHub-Repo (dieses) – **privat** oder **öffentlich**  
- GitHub Actions aktiviert  
- Python 3.12 (nur nötig, wenn lokal getestet wird)  
- Account bei [developer.x.com](https://developer.x.com) für API-Keys  

---

## 🔐 Benötigte Repository Settings

### **Secrets**  
*(Settings → Secrets and variables → Actions → New repository secret)*  
| Name | Beschreibung |
|------|--------------|
| `GH_PAT` | GitHub Personal Access Token (read-only) |
| `X_API_KEY` | API Key von developer.x.com |
| `X_API_SECRET` | API Secret |
| `X_ACCESS_TOKEN` | Access Token |
| `X_ACCESS_TOKEN_SECRET` | Access Token Secret |

### **Variables**  
*(Settings → Secrets and variables → Actions → Variables)*  
| Name | Beispielwert | Beschreibung |
|------|--------------|--------------|
| `GH_USER` | `andrehohenstein` | Dein GitHub-Username |
| `ORGS_CSV` | `Org1,Org2` *(optional)* | Organisationen, die mitgescannt werden |

---

## ⚙️ Verwendung

### **Manuell starten**
1. GitHub → Actions → „Announce new releases on X“ auswählen  
2. **Run workflow** klicken  

### **Automatisch**
- Der Workflow läuft alle **10 Minuten** und prüft auf neue Releases.  
- Bei neuen Releases werden Tweets automatisch gepostet.  

---

## 📝 Best Practices & Sicherheit
- **Keine API-Keys im Code hinterlegen** – nur als GitHub Secrets speichern.  
- **Least Privilege**: PAT nur mit `repo:read` (und `read:org`, falls nötig).  
- **Rotation**: Keys regelmäßig erneuern.  
- **Logs prüfen**: Sicherstellen, dass keine geheimen Daten ausgegeben werden.  

---

## 📜 Changelog
> Änderungen am Projekt werden hier dokumentiert.  
> Vollständige Übersicht: [CHANGELOG.md](CHANGELOG.md)

```
2025-08-07 – Initial Commit: Release-Scanner + X-Poster
```
---

© 2025 André Hohenstein – Microsoft Certified Trainer 💻