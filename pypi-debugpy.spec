#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-debugpy
Version  : 1.8.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/61/fe/0486b90b9ac0d9afced236fdfe6e54c2f45b7ef09225210090f23dc6e48a/debugpy-1.8.0.zip
Source0  : https://files.pythonhosted.org/packages/61/fe/0486b90b9ac0d9afced236fdfe6e54c2f45b7ef09225210090f23dc6e48a/debugpy-1.8.0.zip
Summary  : An implementation of the Debug Adapter Protocol for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-debugpy-license = %{version}-%{release}
Requires: pypi-debugpy-python = %{version}-%{release}
Requires: pypi-debugpy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Parts of IPython, files from: https://github.com/ipython/ipython/tree/rel-1.0.0/IPython
# The files in this package are extracted from IPython to aid the main loop integration
# See tests_mainloop for some manually runable tests

%package license
Summary: license components for the pypi-debugpy package.
Group: Default

%description license
license components for the pypi-debugpy package.


%package python
Summary: python components for the pypi-debugpy package.
Group: Default
Requires: pypi-debugpy-python3 = %{version}-%{release}

%description python
python components for the pypi-debugpy package.


%package python3
Summary: python3 components for the pypi-debugpy package.
Group: Default
Requires: python3-core
Provides: pypi(debugpy)

%description python3
python3 components for the pypi-debugpy package.


%prep
%setup -q -n debugpy-1.8.0
cd %{_builddir}/debugpy-1.8.0
pushd ..
cp -a debugpy-1.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694620909
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-debugpy
cp %{_builddir}/debugpy-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-debugpy/bdaa8bcf57470fae2e892cd2848a7aba3664edf6 || :
cp %{_builddir}/debugpy-%{version}/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/vendored/bytecode-0.13.0.dev0.dist-info/COPYING %{buildroot}/usr/share/package-licenses/pypi-debugpy/7d73b90c1964aabb829818f09bab6a02539765c6 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-debugpy/7d73b90c1964aabb829818f09bab6a02539765c6
/usr/share/package-licenses/pypi-debugpy/bdaa8bcf57470fae2e892cd2848a7aba3664edf6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
