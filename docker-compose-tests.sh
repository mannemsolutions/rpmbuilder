#!/bin/bash
#set -x
set -e

docker-compose down && docker rmi rpmbuilder_rpmbuilder  || echo new install
docker-compose up -d
docker exec rpmbuilder_rpmbuilder_1 /start.sh
