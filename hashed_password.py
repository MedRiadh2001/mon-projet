import hashlib
def hash_password(password):
    # Créer un objet de hachage avec SHA-256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
password = "mysecretpassword"
hashed_password = hash_password(password)
print(f"Mot de passe haché : {hashed_password}")

import os
def hash_password_with_salt(password):
    salt = os.urandom(16)  # Générer un sel aléatoire
    salted_password = password.encode() + salt  # Ajouter le sel au mot de passe
    hashed = hashlib.sha256(salted_password).hexdigest()
    return hashed
salted_hashed_password = hash_password_with_salt(password)
print(f"Mot de passe haché avec sel : {salted_hashed_password}")

