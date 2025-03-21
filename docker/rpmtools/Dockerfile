ARG BASEIMAGE=dontknow:dontcare
FROM ${BASEIMAGE}

RUN dnf update -y && \
    dnf install -y pinentry rpmdevtools rpm-build rpm-sign jq

WORKDIR /usr/rpmbuilder

RUN useradd -G wheel rpmbuilder

USER rpmbuilder
