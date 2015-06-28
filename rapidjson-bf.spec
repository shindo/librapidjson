%global __api_version 1

Name: librapidjson
Version: 1.0.0
Release: 1%{?dist}
Summary: RapidJSON
License: MIT
URL: https://github.com/miloyip/rapidjson
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

# Build dependencies
BuildRequires: valgrind
BuildRequires: cmake >= 2.8.4
BuildRequires: doxygen


%description
A fast JSON parser/generator for C++ with both SAX/DOM style API.


%prep
%setup -q


%build
cd %{_builddir}/%{name}-%{version}/rapidjson
cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DRAPIDJSON_BUILD_EXAMPLES=OFF \
	-DRAPIDJSON_BUILD_THIRDPARTY_GTEST=ON \
	-DRAPIDJSON_HAS_STDSTRING=ON \
	-DCMAKE_CXX_FLAGS=-mno-avx \
	-DINCLUDE_INSTALL_DIR=/usr/include/RapidJSON-%{__api_version} \
	-DCMAKE_INSTALL_DIR=/usr/lib/cmake/RapidJSON-%{__api_version}
make -j $(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 1)


%check
cd %{_builddir}/%{name}-%{version}/rapidjson
ctest -V


%install
rm -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}/rapidjson
%make_install
mv %{buildroot}/usr/lib/pkgconfig/RapidJSON.pc %{buildroot}/usr/lib/pkgconfig/RapidJSON-%{__api_version}.pc


%package -n librapidjson%{__api_version}
Summary: RapidJSON - Development files
Group: Development/Libraries

%description -n librapidjson%{__api_version}
A fast JSON parser/generator for C++ with both SAX/DOM style API.

%files -n librapidjson%{__api_version}
%defattr(-,root,root,-)
%{_includedir}/
%{_prefix}/lib/cmake/
%{_prefix}/lib/pkgconfig/


%package -n librapidjson-doc
Summary: RapidJSON - Documentation files
Group: Documentation
BuildArch: noarch

%description -n librapidjson-doc
A fast JSON parser/generator for C++ with both SAX/DOM style API.

%files -n librapidjson-doc
%defattr(-,root,root,-)
%{_prefix}/share/doc


%clean
rm -rf %{buildroot}


%changelog
* Mon Jun 29 2015 Danil Osherov <shindo@yandex-team.ru> 1.0.0
- Fixes:
- * Fixed a bug in trimming long number sequence
- * Fix double quote in unicode escape
- * Fix negative zero roundtrip (double only)
- * Remove an invalid Document::ParseInsitu() API
- * Remove dead branches and add more unit tests for coverage
- Features:
- * RFC 7159
- * Optional Iterative Parser
- * Deep-copy values
- * Error code and message
- * ASCII Encoding
- * kParseStopWhenDoneFlag
- * kParseFullPrecisionFlag
- * Add Key() to handler concept
- * C++11 compatibility and support
- * Standardize behavior of memcpy() and malloc()
- * Add version macros
- Optimizations
- * Optimized number-to-string and vice versa conversions
- * Short-String Optimization
- * Local stream optimization by traits
- Build
- * Migrating from Premake to CMAKE
- * Remove other JSON libraries for performance comparison
- * Travis & Appveyor Continuous Integration, with Valgrind verification
- * Resolve all warning reports
- Documentation
- * Redo all documentation
- * English, Simplified Chinese
- * Doxygen with Markdown
- * Gitbook

* Mon Apr 13 2015 Danil Osherov <shindo@yandex-team.ru> 0.99.9
- Initial release.
