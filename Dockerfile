FROM rockylinux:8

RUN yum update -y && \
    yum install -y python39 sudo make pinentry rpmdevtools rpm-build

WORKDIR /usr/rpmbuilder

COPY rpmbuilder README.md /usr/rpmbuilder/
COPY scripts /

RUN pip3 install --upgrade pip && pip install --no-cache-dir .
RUN useradd -G wheel rpmbuilder
USER rpmbuilder

CMD github2spec
