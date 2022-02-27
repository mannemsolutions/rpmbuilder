#!/usr/bin/env python3
import os
import yaml
from .githubrepo import githubrepo

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def fromConfig():
    configFile = os.environ.get('GITHUB2SPEC_CONFIG', '/usr/rpmbuilder/conf/github2spec.yaml')
    config = yaml.load(open(configFile), Loader=Loader)
    repos=config['repositories']
    template = open(config['template']).read()
    dest = config.get('dest', '/tmp')
    for name, values in repos.items():
        values['name'] = name
        repo = githubrepo(values, template)
        destFile = os.path.join(dest, name+'.spec')
        print('Writing to {}'.format(destFile))
        with open(destFile, 'w') as specFile:
            specFile.write(repo.recursive_render(template))


if __name__ == '__main__':
    github2spec()
