%global _prefix /usr/local
Summary: Archival and Restoration for Postgres
Name: wal-g-pg
Version: v1.1
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/wal-g/wal-g
Source0: wal-g-pg-ubuntu-18.04-amd64.tar.gz
BuildArch: x86_64
Requires: glibc < 2.29

%description
Archival and Restoration for Postgres

%prep
curl -L https://github.com/wal-g/wal-g/releases/download/v1.1/wal-g-pg-ubuntu-18.04-amd64.tar.gz -o %{_sourcedir}/wal-g-pg-ubuntu-18.04-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/wal-g-pg-ubuntu-18.04-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/wal-g-pg-ubuntu-18.04-amd64 %{buildroot}/%{_bindir}/wal-g-pg


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/wal-g-pg