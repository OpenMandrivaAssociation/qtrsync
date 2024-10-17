%define	AppName	QtRsync

Name:		qtrsync
Version:	alpha.0.1
Release:	4
License:	GPLv2+
URL:		https://www.qt-apps.org/content/show.php/QtRsync?content=75828
Source:		%{AppName}-%{version}.tar.gz
BuildRequires:	qt4-devel
Requires:	rsync
Group:		Networking/WWW
Summary:	Qt4 rsync GUI

%description
QtRsync is a simple qt-based GUI for the rsync tool.

%prep
%setup -qn %{AppName}-%{version}

%build
%qmake_qt4 PREFIX=%{_prefix} 
%make

%install
make install INSTALL_ROOT=%{buildroot}

%clean

%files
%doc INSTALL
%{_bindir}/qtrsync
%{_datadir}/applications/qtrsync.desktop



