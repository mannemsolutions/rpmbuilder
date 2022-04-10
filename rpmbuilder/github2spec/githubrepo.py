#!/usr/bin/env python3
"""
A github repo class that can read a github repo and generate a spec file.
"""
import re
import requests
import jinja2


class GithubRepo(dict):
    """
    Read a github repo and generate a spec file using a jinja2 template
    """
    def __init__(self, values):
        super().__init__()
        # Set some defaults in values, also used to set self['url']
        values['site'] = values.get('site', "github.com")
        values['repository'] = values.get('repository', values['name'])
        values['organization'] = values.get('organization',
                                            values['repository'])

        # These defaults can be overridden from the yaml config if needed
        self['url'] = f'https://{values["site"]}/{values["organization"]}/' \
                      f'{values["repository"]}'
        self['package_arch'] = 'x86_64'
        self['binary_arch'] = 'amd64'
        self['target_release'] = 'latest'
        self['package_name'] = values['name']
        self['asset_filter'] = '{{ name }}-{{ version }}-linux-' \
                               '{{ binary_arch }}.tar.gz$'

        # Copy values into self, get data from github api and overwrite
        # values as needed
        self.update(values)
        self.get_release_info()
        self.update(values)

    def get_repo_info(self):
        """
        Read and return repo on the actual github repo using the github api
        :return: A dictionary with repo info like name, description and license
        """
        url = f'https://api.{self["site"]}/repos/{self["organization"]}/' \
              f'{self["repository"]}'
        result = requests.get(url)
        data = result.json()
        if 'name' not in data:
            raise Exception("Missing 'name' in the return.", data)
        repo_info = {'repo_name': data['name'],
                     'description': data['description'],
                     'license': data['license']['spdx_id']}
        self.update(repo_info)
        return repo_info

    def get_release_info(self):
        """
        Read release info from the actual github repo using the github api
        :return: a dictionary with release info (version, and changelog)
        """
        self.get_repo_info()
        url = f'https://api.{self["site"]}/repos/{self["organization"]}/' \
              f'{self["repository"]}/releases/{self["target_release"]}'
        result = requests.get(url)
        data = result.json()

        self['release_info'] = release_info = {}
        release_info['version'] = data['tag_name'].replace('-', '.')
        release_info['changelog'] = data['body']
        release_info['assets'] = release_assets = []
        self.update(release_info)
        asset_filter = re.compile(self.recursive_render(
            self.get('asset_filter', '.')))
        for asset in data['assets']:
            if asset_filter.search(asset['name']):
                release_assets.append({'name': asset['name'],
                                       'url': asset['browser_download_url']})
        return release_info

    def recursive_render(self, tpl):
        """
        Render a template recursively, so that jinja in jinja is rendered too.
        Use `self` as data
        :param tpl: Template to be rendered
        :return: rendered text
        """
        prev = tpl
        while True:
            curr = jinja2.Template(prev).render(**self)
            if curr != prev:
                prev = curr
            else:
                return curr
