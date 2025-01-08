#!/bin/bash
set -e

cd "$(dirname "$0")"

function github_release_rpms {
	ORG=${2:-mannemsolutions}
	REPO=${1}
	URL="https://api.github.com/repos/${ORG}/${REPO}/releases/latest"
	curl -s "${URL}" | jq --raw-output '.assets[] | .browser_download_url'
}

function minio_rpms {
	for ARCH in amd64 arm64; do
		for T in client/mc server/minio; do
			URL="https://dl.min.io/${T}/release/linux-${ARCH}/"
			curl -s "${URL}" |
				grep -oP '".*202.*\.rpm"' |
				sed 's/"//g' |
				sort |
				tail -n 1 |
				awk '$0="'${URL}'"$0'
		done
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

github_release_rpms wal-g-builder | while read -r RPM; do
	download_rpm "$RPM"
done
