import requests
import sys

URL = "https://raw.githubusercontent.com/MichelPrincy/nante/main/main.py"
TARGET_FILE = "main.py"

print("🌐 Vérification de mise à jour...")

try:
    response = requests.get(URL, timeout=15)

    if response.status_code == 200 and response.text.strip():
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)

        print("✅ Mise à jour installée avec succès.")
        print("➡️ Relancez le bot avec : python main.py")
    else:
        print("❌ Impossible de récupérer le fichier (réponse invalide).")

except Exception as e:
    print("❌ Erreur lors de la mise à jour :", e)

input("\nAppuyez sur Entrée pour quitter...")
sys.exit(0)
