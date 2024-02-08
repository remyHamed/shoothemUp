# Configuration de l'Environnement de Développement Python

## Installation de Python

### Sur Windows

1. Téléchargez le dernier installateur de Python depuis le [site officiel](https://www.python.org/downloads/).
2. Lancez l'installateur. Assurez-vous de cocher la case « Add Python to PATH » avant de cliquer sur « Install Now ».
3. Une fois l'installation terminée, ouvrez l'Invite de Commande et tapez `python --version` pour vérifier que Python est correctement installé.

### Sur macOS

1. Installez Python sur macOS en utilisant [Homebrew](https://brew.sh/), un gestionnaire de paquets pour macOS. Ouvrez le Terminal et tapez :

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Suivez les instructions à l'écran pour terminer l'installation de Homebrew.
2. Après l'installation de Homebrew, installez Python en exécutant :

```
brew install python
```

3. Vérifiez l'installation de Python en tapant `python3 --version` dans le Terminal.

## Configuration de l'Environnement Virtuel

Activez l'environnement virtuel :

- **Sous Unix ou macOS** : Ouvrez votre terminal, puis exécutez :
```
source env/bin/activate
```


- **Sous Windows** : Dans l'invite de commande ou PowerShell, exécutez :
```
.\env\Scripts\Activate.ps1
```

Note : Si vous utilisez l'invite de commande (cmd), utilisez `.\env\Scripts\activate`. Pour PowerShell, si vous rencontrez des restrictions de politique, essayez `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process` avant d'exécuter la commande d'activation.

Installez les dépendances :

```
pip install -r requirements.txt
```


Mettez à jour le fichier de dépendances :

```
pip freeze > requirements.txt

```


Exécution de l'application :

```
python index.py
```

Étape 6 : Désactiver l'Environnement Virtuel
Lorsque vous avez terminé vos travaux dans l'environnement virtuel, vous pouvez le désactiver en utilisant :

```
deactivate
```