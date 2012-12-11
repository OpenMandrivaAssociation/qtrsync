%define	AppName	QtRsync

Name:		qtrsync
Version:	alpha.0.1
Release:	%mkrel 3
License:	GPLv2+
URL:		http://www.qt-apps.org/content/show.php/QtRsync?content=75828
BuildRoot:	%{_tmppath}/%{AppName}-%{version}-%{release}-build
Source:		%{AppName}-%{version}.tar.gz
BuildRequires:	qt4-devel
Requires:	rsync
Group:		Networking/WWW
Summary:	Qt4 rsync GUI

%description
QtRsync is a simple qt-based GUI for the rsync tool.

%prep
%setup -q -n %{AppName}-%{version}

%build
%qmake_qt4 PREFIX=%_prefix 
%make

%install
rm -fr %buildroot
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL
%{_bindir}/qtrsync
%{_datadir}/applications/qtrsync.desktop



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> alpha.0.1-3mdv2011.0
+ Revision: 614686
- the mass rebuild of 2010.1 packages

* Tue Dec 08 2009 Stéphane Téletchéa <steletch@mandriva.org> alpha.0.1-2mdv2010.1
+ Revision: 475194
- import qtrsync


* Tue Nov 03 2009 Donald Stewart <Schultz@mandriva.org> QtRsync-alpha.0.1-2mdv
- add requires
- add buildrequires
* Mon Nov 02 2009 Donald Stewart <schultz@mandriva.org> QtRsync-alpha.0.1-1mdv
- Initial release
