#!/bin/bash

set -e

# INSTAL DEPENDENCIES
sudo pacman -Syy
sudo pacman -S --noconfirm base-devel blas lapack gcc-fortran glpk libxslt
sudo pacman -S --noconfirm python2 python2-pip python2-virtualenv

source python-setup.sh
