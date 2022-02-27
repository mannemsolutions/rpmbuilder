#!/bin/bash
#set -x
set -e

docker-compose down && docker rmi rpmbuilder_rpmbuilder  || echo new install
docker-compose up -d
exit
docker exec rpmbuilder_rpmbuilder_1 /usr/rpmbuilder/bin/start.sh
