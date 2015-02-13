#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for generating documents in EPUB format
Summary(pl.UTF-8):	Biblioteka do generowania dokumentów w formacie EPUB
Name:		libepubgen
Version:	0.0.0
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libepubgen/%{name}-%{version}.tar.xz
# Source0-md5:	21d1d23f609da2e9ed24629b8ae96584
URL:		http://libepubgen.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libepubgen is a library for generating documents in EPUB format,
implementing librevenge document interfaces. It supports conversion of
text documents, presentations and vector drawings.

%description -l pl.UTF-8
libepubgen to biblioteka do generowania dokumentów w formacie EPUB,
implementująca interfejsy dokumentów librevenge. Obsługuje konwersję
dokumentów tekstowych, prezentacji oraz rysunków wektorowych.

%package devel
Summary:	Header files for libepubgen library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libepubgen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel

%description devel
Header files for libepubgen library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libepubgen.

%package static
Summary:	Static libepubgen library
Summary(pl.UTF-8):	Statyczna biblioteka libepubgen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libepubgen library.

%description static -l pl.UTF-8
Statyczna biblioteka libepubgen.

%package apidocs
Summary:	libepubgen API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libepubgen
Group:		Documentation

%description apidocs
libepubgen API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libepubgen.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules \
	--disable-werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libepubgen-*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libepubgen

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libepubgen-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libepubgen-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepubgen-0.0.so
%{_includedir}/libepubgen-0.0
%{_pkgconfigdir}/libepubgen-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libepubgen-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
