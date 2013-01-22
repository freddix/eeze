Summary:	Enlightenment Foundation Library
Name:		eeze
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	1272117074a8a145de5bc57489636ef3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eeze is a library for manipulating devices through udev with a simple
and fast api. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather
device information the instant it becomes known to the system.

%package devel
Summary:	Header files for eeze library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for eeze library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/eeze_*
%attr(755,root,root) %ghost %{_libdir}/libeeze.so.1
%attr(755,root,root) %{_libdir}/libeeze.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeeze.so
%{_includedir}/eeze-1
%{_pkgconfigdir}/eeze.pc

