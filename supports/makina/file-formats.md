# Formats de fichiers

--------------------------------------------------------------------------------

## Plan de formation

- Présentation & Historique
- Syntaxe et bases du langage
- Approche Orientée Objet
- Programmation Orientée Objet en Python
- Librairies standard
- Outils de qualité et tests
- **Formats de fichiers**

--------------------------------------------------------------------------------

## YAML

### Installation

    !console
    $ pip install pyyaml

### Exemple de fichier YAML

    !yaml
    company: Makina Corpus
    technologies:
      - Python
      - Django
      - Drupal

### Lecture du fichier

    !python
    with open("path/to/example.yml") as fp:
        data = yaml.load(fp)
        print(data["technologies"][1])  # Django

--------------------------------------------------------------------------------
