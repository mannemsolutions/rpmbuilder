FROM centos:8

# See https://techglimpse.com/failed-metadata-repo-appstream-centos-8/ for more info
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
    yum update -y && \
    yum install -y python39 rpmbuild sudo make pinentry

WORKDIR /usr/rpmbuilder

COPY rpmbuilder /usr/rpmbuilder/

RUN pip3 install --upgrade pip && pip install --no-cache-dir .
RUN useradd -G wheel rpmbuilder
USER rpmbuilder

CMD github2spec
