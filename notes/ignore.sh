#!/bin/sh 
find -type f -name '*.pyc' -exec rm -f {} ';' 
find -type f -name '.*.swp' -exec rm -f {} ';' 
find -type f -name '*~' -exec rm -f {} ';'
