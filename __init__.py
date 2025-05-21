from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

# Génère une clé une seule fois
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<path:valeur_chiffree>')
def decryptage(valeur_chiffree):
    try:
        valeur_bytes = valeur_chiffree.encode()
        valeur_dechiffree = f.decrypt(valeur_bytes)
        return f"Chaîne déchiffrée : {valeur_dechiffree.decode()}"
    except Exception as e:
        return f"Erreur : la chaîne fournie n'est pas valide ou la clé est incorrecte. Détail : {str(e)}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
