
#Reset PYTHONPATH
unset PYTHONPATH
export PYTHONPATH=/home/modules/versions/64/centos7/pyyaml/pyyaml-3.12/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/netcdf4python/netcdf4python-1.0.7_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/matplotlib/matplotlib-2.0.0_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/numpy/numpy-1.9.1_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/ipython/ipython-3.2.1_gnu4.8.2/lib/python2.7/site-packages

#OPTION 1 - Use note bookfrom IPython
#module load ipython/ipython-2.4


#OPTION 2 - Use latest jupyter notebook using pip & virtualenv

#Set proxy for pip (and others!)
HTTP_PROXY=http://<login>:<psws>@proxy.mercator-ocean.fr:8080
http_proxy=$HTTP_PROXY
HTTPS_PROXY=http://<login>:<psws>@proxy.mercator-ocean.fr:8080
http_proxy=$HTTPS_PROXY

export HTTP_PROXY
export HTTPS_PROXY
export https_proxy
export http_proxy

#Set virtualenv (wrapper)
export WORKON_HOME=$HOME/.virtualenv
source /usr/bin/virtualenvwrapper.sh
