Summary: Archival and Restoration for Postgres
Name: wal-g-pg
Version: v1.1
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/wal-g/wal-g
Source0: wal-g-pg-ubuntu-18.04-amd64.tar.gz
BuildArch: x86_64

%description
Archival and Restoration for Postgres

%prep
prep.sh wal-g-pg

%build
%configure
%make_build

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libsnappy.so*
%{_docdir}/snappy
%exclude %{_libdir}/libsnappy.a
%exclude %{_libdir}/libsnappy.la
