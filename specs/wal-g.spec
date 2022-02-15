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

%changelog
Some interesting features/fixes:
- Include libsodium in the GitHub release builds. Exit with failure if libsodium is requested but WAL-G was not compiled with libsodium support #1062 [CVE-2021-38599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38599)
- UserData is now required to be a valid JSON #1049
- backup-list now sorts backups by the astronomical time of the completition #907

Postgres:
- .history files overwrite prevention fix #1052
- wal-verify can now be run from a standby #1014 
- wal-verify now ignores the permanent backups #1014, #1002

MongoDB:
- Add support for MongoDB 5.0 #1041

SQLServer:
- Fix MSSQL driver import #1038

MySQL:
- Add --turbo flag to disable limiters #1027
- Fix --detailed backup-list bug #1026
- Add --until flag to binlog-push #1005

Redis:
- Add 6.2 support & redis-cli bug workaround #1022

Storages
- S3: customer SSE key support #1042 (https://github.com/wal-g/storages/pull/48)
- Azure: support AZURE_STORAGE_SAS_TOKEN without the leading '?' #1056
- Azure: disable the unnecessary syslog writes #1058
