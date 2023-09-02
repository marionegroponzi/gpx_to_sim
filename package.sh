#!/bin/bash
set -euox pipefail
appname=${PWD##*/}
rm -fr $appname
mkdir $appname
cp *.py $appname
pip install -r requirements.txt --target $appname
# remove un-needed files
rm -fr ${appname}/*.dist-info
# package with zipapp
python -m zipapp -p python $appname
rm -fr $appname

# verify everthing worked
python ./${appname}.pyz --help

