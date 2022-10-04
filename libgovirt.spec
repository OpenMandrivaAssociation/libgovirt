%global major 2
%define libname %mklibname govirt %major
%define devname %mklibname -d govirt
# -*- rpm-spec -*-

%global with_gir 1

Summary: A GObject library for interacting with oVirt REST API
Name: libgovirt
Version: 0.3.9
Release: 1
License: LGPLv2+
Group: Development/C
Source0: http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
URL: http://people.freedesktop.org/~teuf/govirt/
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: meson
BuildRequires: pkgconfig(rest-1.0)
%if %{with_gir}
BuildRequires: gobject-introspection-devel
%endif
#needed for make check
BuildRequires: glib-networking
BuildRequires: dconf
#needed for GPG signature checek
BuildRequires: gnupg2

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n %libname
Summary: A GObject library for interacting with oVirt REST API
Group: System/Libraries
Requires: %name

%description -n %libname
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n %devname
Summary: Libraries, includes, etc. to compile with the libgovirt library
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(glib-2.0)

%description -n %devname
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

Libraries, includes, etc. to compile with the libgovirt library

%prep
#gpgv2 --quiet --keyring %{SOURCE1} %{SOURCE0}
%setup -q

%build
%meson
%meson_builf

%install
%meson_install

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS README

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}{,.*}
%if %{with_gir}
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib
%endif

%files -n %devname
%{_libdir}/%{name}.so
%dir %{_includedir}/govirt-1.0/
%dir %{_includedir}/govirt-1.0/govirt/
%{_includedir}/govirt-1.0/govirt/*.h
%{_libdir}/pkgconfig/govirt-1.0.pc
%if %{with_gir}
%{_datadir}/gir-1.0/GoVirt-1.0.gir
%endif
