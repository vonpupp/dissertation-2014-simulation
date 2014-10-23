#!/bin/sh

set -e

# INSTALL PACKAGES
sudo aptitude update
sudo aptitude -y -q install --without-recommends libblas-dev liblapack3 gfortran \
    libglpk36 libglpk-dev libxml2-dev libxslt1-dev libpng-dev libfreetype6-dev \
    python python-dev python-pip python-virtualenv

source python-setup.sh
