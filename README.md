# Projet python : DANMASHI

par **ARCAS** Manon, **RAFFANEL** Guilhem et **DAUBRESSE** Alexy

I. [Présentation du projet](#i-présentation-du-projet)

II. [Fonctionnalités](#ii-fonctionnalités-disponibles)

III. [Classes](#iii-classes)
1. [Mage](#1-mage)
2. [Assassin](#2-assassin)
1. [Guerrier](#3-guerrier)

IV. [Comment installer le projet](#iv-comment-installer-le-projet)
1. [Installation](#1-installation)
2. [Démarrage](#2-lancement)

___

## I. Présentation du projet :

**Dansmashi** est un jeu d'aventure en CLI !<br>
Vous incarnez un joueur appartenant à une classe de votre choix (mage, guerrier ou assassin) dont le but est de sortir victorieux d'un donjon de 10 étages pleins de monstres. <br>

Chaque niveau est un défi de plus en plus difficile avec des créatures vicieuses à vaincre.<br>
Débloquez de nouvelles compétences et récupérez des objets pour surmonter les épreuves.

## II. Fonctionnalités disponibles :

- Choix du pseudo du personnage ("player" par défault).

- Choix de la classe du personnage parmis : Mage, Assassin et Guerrier.

- Musique de fond durant le jeu.

- Génération aléatoire de 1 à 2 monstres par étage parmi des listes de difficultés différentes afin de varier l'expérience utilisateur (*6 monstres disponibles*).

- ASCII art pour améliorer l'immersion du joueur.

- Choix des attaques grâce aux touches directionnelles.

- Débloquage d'une nouvelle compétence si victoire à l'étage 3

- Récupération d'une potion de vie si victoire contre le boss à l'étage 5.

## III. Classes :

### 1. Mage :

Attaque de base : ***Boule de feu*** <br>

*Description* : lance une boule de feu sur son adversaire.

Attaque de type : ***Protego*** <br>

*Description* : crée un bouclier de protection le rendant invulnérable durant 2 tours.

Attaque spéciale : ***Rayon cosmique*** <br>

*Description* : lance un rayon dévastateur qui fait plus de dégâts qu'une attaque de base mais reçoit des dégâts de recul.

___

### 2. Assassin :

Attaque de base : ***Coup de dagues*** <br>

*Description* : donne un coup de dague à son adversaire.

Attaque de type : **Hachettes des ombres** <br>

*Description* : lance entre 2 et 4 hachettes sur son adversaire (dégâts variables).

Attaque spéciale : **Ecran de fumée** <br>

*Description* : lance un fumigène et rend confus son adversaire lui empêchant de bien viser pendant 2 tours.

___

### 3. Guerrier :

Attaque de base : **Déferlement** <br>

*Description* : déclanche un enchaînement d'attaque vives sur son adversaire.

Attaque de type : **Canalisation** <br>

*Description* : se canalise pour augmenter sa puissance d'attaque (*! ne peut être utilisé qu'une fois sinon perd son tour !*).

Attaque spéciale : **Colère du Berserkeur** <br>

*Description* : déclenche sa colère du Berserkeur au risque d'être blessé (1 chance sur 2). <br> Récupère une vie de 15 si sa vie actuelle est inférieure à 10 hp, puis lance une quantité de dégâts dépendante de ses points de vie.

## IV. Comment installer le projet :

### 1. Installation :

Cloner le repository avec la commande suivante :
```bash
git clone https://github.com/Manon-Arc/Projet_python_Danmashi.git
```
Se rendre dans le dossier :
```bash
cd Projet_python_Danmashi
```
Installer les librairie necéssaires :
```python
pip install -r requirement.txt
```

### 2. Lancement :

Exécuter la commande suivante :
```python
python .\engine.py
```

😉 Enjoy !