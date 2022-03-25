#!/bin/bash
github2spec
for SPEC in /host/specs/*.spec; do
  rpmbuild -ba "${SPEC}"
done
cp /home/rpmbuilder/rpmbuild/RPMS/*/*.rpm /host/rpms/
