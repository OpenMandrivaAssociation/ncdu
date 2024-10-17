Name:		ncdu
Version:	1.15.1
Release:	1
Summary:	Text-based disk usage viewer

Group:		Monitoring
License:        MIT
URL:            https://dev.yorhel.nl/ncdu/
Source0:        http://dev.yorhel.nl/download/%{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_mandir}/man1/ncdu.1.*
%doc COPYING ChangeLog
%{_bindir}/ncdu
