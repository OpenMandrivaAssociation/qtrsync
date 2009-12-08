%define	AppName	QtRsync

Name:		qtrsync
Version:	alpha.0.1
Release:	%mkrel 2
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

