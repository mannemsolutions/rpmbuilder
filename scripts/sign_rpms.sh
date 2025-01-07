#!/bin/bash
set -e

[ ! -d /host/secrets ] && exit 0

[ -e /host ] && DEST=/host || DEST=/tmp
cd "$DEST"
export RPMDEST=${RPMDEST:-${DEST}/rpms}

sed "s/PASSPHRASE/${GPG_PASSPHRASE}/" config/rpmmacros >~/.rpmmacros
echo "Importing pubkey..."
gpg --import --no-tty --batch --yes <gpg_pubkey.asc
echo "Importing seckey..."
gpg --import --no-tty --batch --yes </host/secrets.org/GPG_KEY.bin
echo "rpmsign --addsign..."
rpmsign --addsign rpms/*.rpm

echo Siging finished succesfully
