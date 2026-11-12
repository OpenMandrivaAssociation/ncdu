Name:		ncdu
Version:	1.22
Release:	1
Summary:	Text-based disk usage viewer

Group:		Monitoring
License:        MIT AND Zlib
URL:            https://dev.yorhel.nl/ncdu/
Source0:        https://dev.yorhel.nl/download/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(ncursesw)

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup -q
sed -n '1,/^[[:space:]]*\*\//p' deps/khashl.h > COPYING.khashl
sed -n '1,/^[[:space:]]*\*\//p' deps/strnatcmp.c > COPYING.strnatcmp

%build
%configure
%make_build

%install
%make_install

%files
%{_mandir}/man1/ncdu.1.*
%doc ChangeLog
%license COPYING COPYING.khashl COPYING.strnatcmp
%{_bindir}/ncdu
