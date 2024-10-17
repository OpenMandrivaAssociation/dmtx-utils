Name:		dmtx-utils
Version:	0.7.4
Release:	4
Summary:	a library for reading and writing Data Matrix 2D barcodes
Source0:	http://downloads.sourceforge.net/project/libdmtx/libdmtx/0.7.4/%{name}-%{version}.tar.bz2
Group:		Development/C++
License: 	GPLv2
URL:		https://www.libdmtx.org
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libdmtx)
Obsoletes: libdmtx-utils

%description
dmtx-utils is open source software for reading and writing Data Matrix 2D
barcodes on Linux and Unix. At its core libdmtx is a shared library,
allowing C/C++ programs to use its capabilities without restrictions
or overhead.

This package contains command line tools (dmtxread, dmtxwrite and dmtxquery)
to test %{name} and to learn its behavior.

%prep
%setup -q

%build
%configure2_5x \

%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING README README.linux TODO
%{_bindir}/dmtxquery
%{_bindir}/dmtxread
%{_bindir}/dmtxwrite
%{_mandir}/man1/dmtxquery*
%{_mandir}/man1/dmtxread*
%{_mandir}/man1/dmtxwrite*


%changelog
* Sat Dec 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.7.4-2
+ Revision: 745082
- rebuild to properly obsolete old utils pkg name
- removed unneeded BRs
- first build for spit out dmxt-utils from lib
- copy dmtx-utils now split out from libdmtx
- new version 0.7.4.tar.bz2
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2
+ Revision: 660235
- mass rebuild

  + John Balcaen <mikala@mandriva.org>
    - Remove BuildRoot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Buildrequires

* Tue Aug 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 574836
- import libdmtx

