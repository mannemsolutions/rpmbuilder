#!/bin/bash
set -e

cd "$(dirname "$0")"

function minio_rpms {
	for T in client/mc server/minio; do
		URL="https://dl.min.io/${T}/release/linux-amd64/"
		curl -s "${URL}" |
			grep -oP '".*202.*\.rpm"' |
			sed 's/"//g' |
			sort |
			tail -n 1 |
			awk '$0="'${URL}'"$0'
	done
}

function download_rpm {
	URL=$1
	BASENAME=$(basename "$URL")
	[ -e "$BASENAME" ] && return 0
	curl -OL "$URL"
}

cd /host/rpms

minio_rpms | while read -r RPM; do
	download_rpm "$RPM"
done
