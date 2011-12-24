Name:		dmtx-utils
Version:	0.7.4
Release:	1
Summary:	a library for reading and writing Data Matrix 2D barcodes
Source0:	http://downloads.sourceforge.net/project/libdmtx/libdmtx/0.7.4/%{name}-%{version}.tar.bz2
Group:		Development/C++
License: 	GPLv2
URL:		http://www.libdmtx.org
BuildRequires:  tiff-devel
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libpng15)

%description
dmtx-utils is open source software for reading and writing Data Matrix 2D barcodes
on Linux and Unix. At its core libdmtx is a shared library, allowing C/C++
programs to use its capabilities without restrictions or overhead.

This package contains command line tools (dmtxread, dmtxwrite and dmtxquery)
to test %{name} and to learn its behavior.

%prep
%setup -q

%build
%configure2_5x \

%make

%install
rm -rf %{buildroot}
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING README README.linux TODO
%{_bindir}/dmtxquery
%{_bindir}/dmtxread
%{_bindir}/dmtxwrite
%{_mandir}/man1/dmtxquery*
%{_mandir}/man1/dmtxread*
%{_mandir}/man1/dmtxwrite*
