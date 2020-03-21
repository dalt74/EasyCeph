%define version 1.0.2

%global debug_package %{nil}

BuildArch:	noarch

Name:		easyceph
Version:	%{version}
Release:	1
Summary:	EasyCeph - ceph management tools bundle
License:	GPLv2
URL:		http://github.com/dalth74/EasyCeph

Source:		%{name}-%{version}.tar.gz

Requires:	ceph-common
Requires:	ceph-mon
Provides:	ceph-mds
Requires:	ceph-mgr
Requires:	ceph-mds
Requires:	ceph-osd

%description
EasyCeph - ceph management tools
%prep
%setup -q -n %{name}-%{version}

%build
echo Fake build

%install
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/lib/systemd/system
cp bin/ec-* %{buildroot}/bin
cp ximera/bin/* %{buildroot}/bin
cp ximera/systemd/* %{buildroot}/usr/lib/systemd/system

%clean
rm -rf %{buildroot}

%post
systemctl daemon-reload

%postun
systemctl daemon-reload

%files
%attr(755,root,root) /bin/*
%attr(644,root,root) /usr/lib/systemd/system/ximera-*

%changelog
* Fri Mar  6 2020 Artemy Kapitula <dalt74@gmail.com>
- Initial build
