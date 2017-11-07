#! /bin/bash

#Init jupyter virtualenv
mkvirtualenv --system-site-packages jupyter

echo You are now working on $(which python)


#upgrade libs
pip install -U backports.ssl_match_hostname
pip install -U IPython

#install jupyter
pip install jupyter


echo "Jupyter has been installed"