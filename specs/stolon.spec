%global _prefix /usr/local
Summary: PostgreSQL cloud native High Availability and more.
Name: stolon
Version: v0.17.0
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/sorintlab/stolon
Source0: stolon-v0.17.0-linux-amd64.tar.gz
BuildArch: x86_64

%description
PostgreSQL cloud native High Availability and more.

%prep
curl -L https://github.com/sorintlab/stolon/releases/download/v0.17.0/stolon-v0.17.0-linux-amd64.tar.gz -o %{_sourcedir}/stolon-v0.17.0-linux-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/stolon-v0.17.0-linux-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/stolon-*-linux-amd64/bin/stolonctl %{buildroot}/%{_bindir}/stolonctl
%{__install} -m 0755 %{_builddir}/stolon-*-linux-amd64/bin/stolon-sentinel %{buildroot}/%{_bindir}/stolon-sentinel
%{__install} -m 0755 %{_builddir}/stolon-*-linux-amd64/bin/stolon-proxy %{buildroot}/%{_bindir}/stolon-proxy
%{__install} -m 0755 %{_builddir}/stolon-*-linux-amd64/bin/stolon-keeper %{buildroot}/%{_bindir}/stolon-keeper


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/stolonctl
%{_bindir}/stolon-sentinel
%{_bindir}/stolon-proxy
%{_bindir}/stolon-keeper
