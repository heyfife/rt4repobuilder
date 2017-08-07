#!/bin/bash

MODULE=$1
FOLDER=$(echo "perl-$MODULE-srpm" | tr -s '::' '-')

if [ -d $FOLDER ]
then
  echo "Existing module found. aborting. In folder $FOLDER"
  exit 1
fi

mkdir $FOLDER
cd $FOLDER
$(cpanspec $MODULE)

ln -s ../defaultModuleGitIgnore .gitignore

# Default to EPEL-only build. if in dependency chain, will require
# manual intervention anyway
ln -s ../Makefile.epel Makefile
