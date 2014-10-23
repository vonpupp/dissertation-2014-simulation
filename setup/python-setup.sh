#!/bin/bash

set -e

PIP_CACHE='.pipcache'

# source spawns on the current shell and exits, so we need this workaround
# http://stackoverflow.com/a/13122219
activate() {
    source env/bin/activate
}

# CREATE VIRTUAL ENV
if hash virtualenv2 2>/dev/null; then
    virtualenv2 env
else
    virtualenv env
fi

# ACTIVATE VIRTUAL ENV
activate

# PYTHON PIP PACKAGES
mkdir -p "${PIP_CACHE}"
pip install --download-cache "${PIP_CACHE}" lxml==3.4.0
pip install --download-cache "${PIP_CACHE}" numpy==1.9.0
pip install --download-cache "${PIP_CACHE}" FuncDesigner==0.5402
pip install --download-cache "${PIP_CACHE}" openopt==0.5402
pip install --download-cache "${PIP_CACHE}" matplotlib==1.4.0
pip install --download-cache "${PIP_CACHE}" inspyred==1.0
export CVXOPT_BUILD_GLPK=1 && pip install --download-cache "${PIP_CACHE}" cvxopt==1.1.7
