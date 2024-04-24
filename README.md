# Python Project: DANMASHI

by **ARCAS** Manon <br>

___

ℹ️ **Warning**: This game is in French!

I. [Project Overview](#i-project-overview)

II. [Features](#ii-available-features)

III. [Classes](#iii-classes)
   1. [Mage](#1-mage)
   2. [Assassin](#2-assassin)
   3. [Warrior](#3-warrior)

IV. [How to Install the Project](#iv-how-to-install-the-project)
   1. [Installation](#1-installation)
   2. [Running](#2-running)

___

## I. Project Overview:

**DANMASHI** is a CLI adventure game!<br>
You embody a player belonging to a class of your choice (mage, warrior, or assassin) whose goal is to emerge victorious from a dungeon with 10 floors filled with monsters. <br>

Each level is an increasingly difficult challenge with vicious creatures to defeat.<br>
Unlock new skills and collect items to overcome the trials.

## II. Available Features:

- Choice of character's nickname ("player" by default).
- Choice of character class among: Mage, Assassin, and Warrior.
- Background music during the game.
- Random generation of 1 to 2 monsters per floor from different difficulty lists to vary the user experience (*6 available monsters*).
- ASCII art to enhance player immersion.
- Action selection using directional keys.
- Unlocking a new skill if victory on floor 3.
- Recovery of a life potion (life restored to maximum) if victory against the boss on floor 5.

## III. Classes:

### 1. Mage:

- Basic Attack: **Fireball** <br>
  *Description*: throws a fireball at the opponent.
  
- Type Attack: **Protego** <br>
  *Description*: creates a protective shield making it invulnerable for 2 turns (*! reset at each floor change if active !*).
  
- Special Attack: **Cosmic Ray** <br>
  *Description*: unleashes a devastating ray that inflicts more damage than a basic attack but receives recoil damage.

### 2. Assassin:

- Basic Attack: **Dagger Strike** <br>
  *Description*: strikes the opponent with a dagger.
  
- Type Attack: **Shadow Axes** <br>
  *Description*: throws between 2 and 4 axes at the opponent (variable damage).
  
- Special Attack: **Smoke Screen** <br>
  *Description*: throws a smoke bomb and confuses the opponent, preventing accurate aiming for 2 turns (*! reset at each floor change if active !*).

### 3. Warrior:

- Basic Attack: **Rampage** <br>
  *Description*: unleashes a flurry of swift attacks on the target.
  
- Type Attack: **Channeling** <br>
  *Description*: channels to increase attack power (*! can only be used once per floor otherwise loses turn !*).
  
- Special Attack: **Berserker's Wrath** <br>
  *Description*: triggers the berserker's wrath at the risk of being injured (1 in 2 chance). <br> Recovers 15 hp if current life is less than 5 hp, then deals damage dependent on remaining hit points.

## IV. How to Install the Project:

### 1. Installation:

Clone the repo using the following command:
```bash
git clone https://github.com/Manon-Arc/Projet_python_Danmashi.git
