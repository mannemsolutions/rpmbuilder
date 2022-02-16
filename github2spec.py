#!/usr/bin/env python
import requests
import re
import os.path
import yaml

import jinja2

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def recursive_render(tpl, values):
     prev = tpl
     while True:
         curr = jinja2.Template(prev).render(**values)
         if curr != prev:
             prev = curr
         else:
             return curr


class githubrepo(dict):
    def __init__(self, values):
        # Set some defaults in values, also used to set self['url']
        values['site'] = values.get('site', "github.com")
        values['repository'] = values.get('repository', values['name'])
        values['organization'] = values.get('organization', values['repository'])

        # These defaults can be overridden from the yaml config if needed
        self['url'] = 'https://{site}/{organization}/{repository}'.format(**values)
        self['package_arch'] = 'x86_64'
        self['binary_arch'] = 'amd64'
        self['target_release'] = 'latest'
        self['package_name'] = values['name']
        self['asset_filter'] = '{{ name }}-{{ version }}-linux-{{ binary_arch }}.tar.gz$'

        # Copy values into self, get data from github api and overwrite anything from values if needed
        self.update(values)
        self.get_release_info()
        self.update(values)

    def get_repo_info(self):
        url = 'https://api.{site}/repos/{organization}/{repository}'.format(**self)
        result = requests.get(url)
        data = result.json()
        if 'name' not in data:
            raise Exception("I expected 'name' in the return, but didn't.", data)
        repo_info = {}
        repo_info['repo_name'] = data['name']
        repo_info['description'] = data['description']
        repo_info['license'] = data['license']['spdx_id']
        self.update(repo_info)
        return repo_info
    
    def get_release_info(self):
        self.get_repo_info()
        url = 'https://api.{site}/repos/{organization}/{repository}/releases/{target_release}'.format(**self)
        result = requests.get(url)
        data = result.json()

        self['release_info'] = release_info = {}
        release_info['version'] = data['tag_name'].replace('-', '.')
        release_info['changelog'] = data['body']
        release_info['assets'] = release_assets = []
        self.update(release_info)
        asset_filter = re.compile(recursive_render(self.get('asset_filter', '.'), self))
        for asset in data['assets']:
            if asset_filter.search(asset['name']):
                release_assets.append({ 'name': asset['name'], 'url': asset['browser_download_url']})
        return release_info


def main():
    repos = yaml.load(open('github2spec.yaml'), Loader=Loader)
    for name, values in repos.items():
        values['name'] = name
        repo = githubrepo(values)
        template = open('templates/spec.j2').read()
        with open(os.path.join('specs', name+'.spec'), 'w') as specfile:
            specfile.write(recursive_render(template, repo))


if __name__ == '__main__':
    main()

