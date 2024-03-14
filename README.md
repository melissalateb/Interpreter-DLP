# Analyseur de Code JavaScript

Ce projet vise à développer un analyseur de code en Python pour évaluer la qualité du code JavaScript. Il comprend plusieurs étapes telles que l'analyse syntaxique, la tokenization, et le scoring, chacune étant implémentée dans des modules distincts.

## Structure du Projet

- **Parser** : Ce module est responsable de l'analyse syntaxique du code JavaScript pour créer l'Arbre Syntaxique Abstrait (AST).
- **Tokenizer** : Cette partie du projet convertit le code JavaScript en une série de tokens significatifs.
- **Scoring** : Le module de scoring évalue la qualité du code en fonction de différents critères prédéfinis.

## Utilisation

1. Cloner le dépôt : `git clone https://gitlab.com/mustafais481/code-analyzer.git`
2. Lancer le fichier main : `python3 main.py`


## Fonctionnalités

- **Tokenization** : Division du code JavaScript en tokens significatifs tels que les mots-clés, les identificateurs, les nombres, etc.
- **Analyse Syntaxique (parser)** : Création de l'Arbre Syntaxique Abstrait (AST) pour représenter la structure du code JavaScript.
- **Scoring** : Évaluation de la qualité du code en attribuant des scores basés sur des critères comme l'utilisation des variables, l'indentation, etc.

## Statut du Projet

Le développement est actif et en cours. Des améliorations continues sont apportées pour améliorer la précision et les fonctionnalités de l'analyseur de code.
