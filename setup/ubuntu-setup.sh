# INSTALL PACKAGES
sudo aptitude update
sudo aptitude -y -q install --without-recommends liblapack3 gfortran libglpk36 \
    libxml2-dev libxslt1-dev python-dev \

# CREATE PIP CACHE
mkdir ~/.pipcache

# INSTALL PIP PACKAGES sudo pip install --download-cache ~/.pipcache
# numpy==1.9.0
sudo pip install --download-cache ~/.pipcache FuncDesigner==0.5402
sudo pip install --download-cache ~/.pipcache openopt==0.5402
sudo pip install --download-cache ~/.pipcache matplotlib==1.3.1
sudo pip install --download-cache ~/.pipcache inspyred==1.0
sudo pip install --download-cache ~/.pipcache lxml==3.4.0

export CVXOPT_BUILD_GLPK=1 && pip install --download-cache ~/.pipcache --user cvxopt==1.1.7
