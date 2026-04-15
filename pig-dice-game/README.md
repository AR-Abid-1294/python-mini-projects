# 🎲 Pig Dice Game

A simple command-line multiplayer dice game built with Python.
Players take turns rolling a dice and try to reach the winning score while avoiding penalties and risky rolls.

---

## 📌 Overview

This game is a digital version of the classic **Pig Dice Game**.
It supports multiple players and includes special rules that add strategy and risk to each turn.

---

## 🧠 Game Rules

- Each player rolls a six-sided dice (1–6) during their turn.
- If a player rolls **1**:
  - They lose all points collected in that turn.
  - Their turn immediately ends.
- Players can choose after each roll:
  - **Roll again (y)** to increase turn points
  - **Stop (n)** to save turn points to total score
- Special rule:
  - If a player rolls **two consecutive 6s**, their total score resets to **0**.
- The first player to reach or exceed the **winning score** wins the game.

---

## 🚀 How to Run

### Requirements
- Python 3.x

### Run the game
```bash
python pig-dice-game.py
