#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kgamma
Version  : 6.3.3
Release  : 20
URL      : https://download.kde.org/stable/plasma/6.3.3/kgamma-6.3.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.3/kgamma-6.3.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.3/kgamma-6.3.3.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kgamma-data = %{version}-%{release}
Requires: kgamma-lib = %{version}-%{release}
Requires: kgamma-license = %{version}-%{release}
Requires: kgamma-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : ki18n-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kgamma package.
Group: Data

%description data
data components for the kgamma package.


%package doc
Summary: doc components for the kgamma package.
Group: Documentation

%description doc
doc components for the kgamma package.


%package lib
Summary: lib components for the kgamma package.
Group: Libraries
Requires: kgamma-data = %{version}-%{release}
Requires: kgamma-license = %{version}-%{release}

%description lib
lib components for the kgamma package.


%package license
Summary: license components for the kgamma package.
Group: Default

%description license
license components for the kgamma package.


%package locales
Summary: locales components for the kgamma package.
Group: Default

%description locales
locales components for the kgamma package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kgamma-6.3.3
cd %{_builddir}/kgamma-6.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742543042
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742543042
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgamma
cp %{_builddir}/kgamma-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kgamma/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kgamma-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kgamma/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcmkgamma

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_kgamma.desktop
/usr/share/kgamma/pics/background.png
/usr/share/kgamma/pics/cmyscale.png
/usr/share/kgamma/pics/darkgrey.png
/usr/share/kgamma/pics/greyscale.png
/usr/share/kgamma/pics/lightgrey.png
/usr/share/kgamma/pics/midgrey.png
/usr/share/kgamma/pics/rgbscale.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/cs/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/cs/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/de/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/en/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/es/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/et/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/fr/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/id/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/it/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/nl/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/pt/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/ru/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/sl/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/sl/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/sv/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/tr/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/kgamma/index.docbook
/usr/share/doc/HTML/uk/kcontrol/kgamma/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/kgamma/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/plasma/kcminit/kcm_kgamma_init.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kgamma/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kgamma/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kcmkgamma.lang
%defattr(-,root,root,-)

