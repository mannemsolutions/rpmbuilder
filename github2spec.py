#!/usr/bin/env python
import requests
import re

def get_repo_info(repo):
    url = repo
    # e.a. https://github.com/wal-g/wal-g/releases/latest

    result = requests.get(url)
    data = result.json()
    #print(data)
    repo_info = {
        'description': data['description'],
        'license': data['license']['spdx_id']
    }

    #data = open('wal-g.latest').read()
    return repo_info

def get_release_info(repo, asset_filter):
    release_info = get_repo_info(repo)
    url = repo+'/releases/latest'
    # e.a. https://github.com/wal-g/wal-g/releases/latest

    result = requests.get(url)
    data = result.json()
    #data = open('wal-g.latest').read()
    #print(data)
    release_info['release'] = data['name'],
    release_info['changelog'] = data['body']
    release_info['assets'] = release_assets = {}
    re_asset = re.compile(asset_filter)
    for asset in data['assets']:
        if re_asset.search(asset['name']):
            print(asset['name'])
            release_assets[asset['name']] = asset['url']

    return release_info


'''
wal-g:
  summary: Snappy, a fast compressor/decompressor.
  version: 1.1.3
  release: 1%{?dist}
  license: BSD
  group: Development/Libraries
  url: https://github.com/google/snappy
  source:
  - %{name}-%{version}.tar.gz
  buildArch: x86_64
  description: Snappy is a compression/decompression library. It does not aim for maximum compression, or compatibility with any other compression library; instead, it aims for very high speeds and reasonable compression. For instance, compared to the fastest mode of zlib, Snappy is an order of magnitude faster for most inputs, but the resulting compressed files are anywhere from 20% to 100% bigger.
  files:
   - %{_libdir}/libsnappy.so*
   - %{_docdir}/snappy
   - %exclude %{_libdir}/libsnappy.a
   - %exclude %{_libdir}/libsnappy.la
  changelog:
  * Tue Oct 10 2017 - S. Mannem <smannem@bol.com>
  - Initial build of this spec
'''




def main():
    rel_info = get_release_info('https://api.github.com/repos/wal-g/wal-g', 'wal-g-pg-.*-amd64.tar.gz')
    print(rel_info)
#    repo_info = get_repo_info('https://api.github.com/repos/wal-g/wal-g')
#    print(repo_info)


if __name__ == '__main__':
    main()

