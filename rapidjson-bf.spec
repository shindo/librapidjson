%global __api_version 0

Name: rapidjson
Version: 0.99.9
Release: 1%{?dist}
Summary: RapidJSON
License: MIT
URL: https://github.com/miloyip/rapidjson
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

# Build dependencies
BuildRequires: gtest-devel
BuildRequires: valgrind

# CMake workaround
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires: cmake28
%global __cmake %{cmake28}
%global __ctest ctest28
%else
BuildRequires: cmake
%global __cmake %{cmake}
%global __ctest ctest
%endif

%description
A fast JSON parser/generator for C++ with both SAX/DOM style API.


%prep
%setup -q
cd %{_builddir}/%{name}-%{version}
patch -p1 --verbose < patch/test-CMakeLists.txt.patch
patch -p1 --verbose < patch/test-unittest.patch


%build
cd %{_builddir}/%{name}-%{version}/rapidjson
%{__cmake} -DCMAKE_INSTALL_PREFIX=/usr \
	-DRAPIDJSON_BUILD_DOC=OFF \
	-DRAPIDJSON_HAS_STDSTRING=ON \
	-DCMAKE_CXX_FLAGS=-mno-avx
make -j $(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 1)


%check
cd %{_builddir}/%{name}-%{version}/rapidjson
%{__ctest} -V


%install
rm -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}/rapidjson
%make_install


%package -n librapidjson%{__api_version}-devel
Summary: RapidJSON - Development files
Group: Development/Libraries

%description -n librapidjson%{__api_version}-devel
A fast JSON parser/generator for C++ with both SAX/DOM style API.

%files -n librapidjson%{__api_version}-devel
%defattr(-,root,root,-)
%{_includedir}/rapidjson/


%clean
rm -rf %{buildroot}


%changelog
* Mon Apr 13 2015 Danil Osherov <shindo@yandex-team.ru> 0.99.9
- Initial release.
