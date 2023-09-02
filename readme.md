## Overview
This app opens the iPhone Simulator, reads a gpx file passed in as parameter 'file' and inject the waypoints to the simulator with a walking speed.
It contains a package.sh script to generate a pyz 'executable'.

## On a fresh clone
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
...
deactivate
```

### Note
Configure the Python interpreter in intelliJ (with Python CE plugin) by selecting the python executable in the venv folder

### ref. [how to create deployable packages](https://www.infoworld.com/article/3656628/6-ways-to-package-python-apps-for-re-use.html)

## Create standalone package with zipapp
See package.sh

