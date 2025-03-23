#!python3

'''
This module is meant to create a matrix of all specs, all arch'es, all bases and all versions.
'''

import json
from os import listdir
from os.path import isfile, join

armspecs = [f for f in listdir('./specs') if isfile(join('./specs', f)) if 'aarch64' in f]
amdspecs = [f for f in listdir('./specs') if isfile(join('./specs', f)) if 'x86_64' in f]

images = [ ('fedora','42','amd64') ]
images += [ ('rockylinux','9','arm64') ]

matrix = [ {'arch': arch, 'baseimage': base, 'version': version, 'spec': spec}
    for spec in amdspecs for base, version, arch in images if arch == 'amd64' ]
matrix += [ {'arch': arch, 'baseimage': base, 'version': version, 'spec': spec}
    for spec in armspecs for base, version, arch in images if arch == 'arm64' ]
print('mymatrix='+json.dumps({'include':matrix}))
