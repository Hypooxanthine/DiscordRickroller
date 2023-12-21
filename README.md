# DiscordRickroller

Transformez un texte en un message discord où chaque mot est un lien vers [Never Gonna Give You Up - Rick Astley (YouTube)](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

## Screens

![Screen](/Images/Screen.png)

## Dépendances

Fait en Python.

- tkinter
- pyperclip

## Fonctionnement

Entrez votre message tel que vous voulez qu'il soit affiché dans Discord. Cliquez sur le bouton "Rickrolliser". Le texte formaté apparaît en-dessous et est inséré dans votre presse-papier en même temps. Vous n'avez plus qu'à CTRL+V dans un salon Discord.

Le formatage `[mot](<url>)` plutôt que `[mot](url)` permet de ne pas afficher la preview de la video dans votre message, ce qui gâcherait bien sûr l'effet de surprise.

## Pourquoi chaque mot est un lien plutôt que le message entier ?

Car je trouve ça plus drôle.
