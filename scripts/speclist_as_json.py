#!python3

'''
This module is meant to create a matrix of all specs, all arch'es, all bases and all versions.
'''

import json
from os import listdir
from os.path import isfile, join

armspecs = [f for f in listdir('./specs') if isfile(join('./specs', f)) if 'aarch64' in f]
amdspecs = [f for f in listdir('./specs') if isfile(join('./specs', f)) if 'x86_64' in f]

arches =['amd64','arm64']
images = [ ('fedora',str(version)) for version in range(39,42)]
images += [ ('rockylinux',str(version)) for version in range(8,9)]

matrix = [ {'arch': 'amd64', 'baseimage': base, 'version': version, 'spec': spec}
    for spec in amdspecs for base, version in images ]
matrix += [ {'arch': 'arm64', 'baseimage': base, 'version': version, 'spec': spec}
    for spec in armspecs for base, version in images ]

print('mymatrix='+json.dumps({'include':matrix}))
