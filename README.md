# Démonstration de vulnérabilité XSS

Ce projet est une simple application Flask qui démontre une vulnérabilité de type Cross-Site Scripting (XSS). Il s'agit d'un système de commentaires basique où les utilisateurs peuvent poster des commentaires qui sont affichés à tout le monde.

## Comment ça fonctionne

L'application dispose d'une seule page où les utilisateurs peuvent soumettre des commentaires via un formulaire. Les commentaires sont stockés dans une liste sur le serveur et sont rendus directement dans le HTML de la page. Ce rendu direct des entrées des utilisateurs crée une vulnérabilité XSS.

## Comment exécuter le projet

### Localement avec Python

Pour exécuter l'application localement, suivez ces étapes :

1. Clonez le répo.
2. Installez les dépendances avec `pip install -r requirements.txt`.
3. Lancez le serveur avec `python server.py`.

### Localement avec Docker
Vous pouvez également exécuter l'application en utilisant Docker. Voici les étapes :

1. Construisez l'image Docker : `docker build -t xss-demo .`
2. Lancez le conteneur Docker : `docker run -p 5000:5000 xss-demo`

## Comment tester la vulnérabilité XSS

Vous pouvez tester la vulnérabilité XSS en postant un commentaire qui inclut du code JavaScript.
Par exemple, vous pourriez poster le commentaire `<script>alert('XSS')</script>`.

## Démonstration en direct

Vous pouvez voir une démonstration en direct de l'application à [https://xss-production.up.railway.app](https://xss-production.up.railway.app).
