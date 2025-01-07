FROM rockylinux:9

RUN dnf update -y && \
    dnf install -y python3-pip sudo make pinentry rpmdevtools rpm-build rpm-sign cmake bind-utils git iproute golang && \
    dnf groupinstall -y "Development Tools"

WORKDIR /usr/rpmbuilder

COPY rpmbuilder README.md /usr/rpmbuilder/
COPY scripts /

RUN /usr/bin/pip3 install --upgrade pip && /usr/bin/pip3 install --no-cache-dir .
RUN useradd -G wheel rpmbuilder

USER rpmbuilder

CMD github2spec
