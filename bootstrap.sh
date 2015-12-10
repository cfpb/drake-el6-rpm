#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install java-1.8.0-openjdk

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
    SCRIPTPATH=/vagrant
fi

mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES
wget https://raw.usercontent.com/Factual/drake/1.0.1/bin/drake
