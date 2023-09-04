# FizzBuzz avec tests et GitHub Actions
Ce projet présente une implémentation simple de l'exercice de programmation FizzBuzz en Python, avec des tests unitaires et une configuration GitHub Actions pour exécuter ces tests à chaque push sur la branche main.

## Problème de FizzBuzz
Écrire une fonction `fizzBuzz` qui prend un nombre entier en entrée et retourne :

* "Fizz" si le nombre est un multiple de 3,
* "Buzz" si le nombre est un multiple de 5,
* "FizzBuzz" si le nombre est un multiple de 3 et de 5,
* Le nombre lui-même sous forme de chaîne de caractères sinon.

## Implémentation en Python
Voici une implémentation simple de la fonction en Python :


```python
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
```

## Tests unitaires en Python
Nous utilisons le module unittest de Python pour les tests unitaires :

```python
import unittest

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(6), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")
    # ...
```

## GitHub Actions
Pour ajouter une action GitHub qui exécute ces tests à chaque push sur la branche `main`, suivez ces étapes :

* Dans votre dépôt GitHub, accédez à .github/workflows ou créez ces dossiers si nécessaire.
* Créez un nouveau fichier YAML, par exemple python-test.yml.
* Ajoutez la configuration suivante dans ce fichier :
```yaml
name: Python Tests

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install Dependencies
      run: pip install -r requirements.txt

    - name: Run Tests
      run: python -m unittest discover
```
Poussez ce fichier sur la branche main de votre dépôt GitHub.