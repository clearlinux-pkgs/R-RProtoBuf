#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RProtoBuf
Version  : 0.4.17
Release  : 23
URL      : https://cran.r-project.org/src/contrib/RProtoBuf_0.4.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RProtoBuf_0.4.17.tar.gz
Summary  : R Interface to the 'Protocol Buffers' 'API' (Version 2 or 3)
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RProtoBuf-lib = %{version}-%{release}
Requires: R-RCurl
Requires: R-Rcpp
BuildRequires : R-RCurl
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : protobuf-dev

%description
efficient yet extensible format. Google uses Protocol Buffers for almost all
 of its internal 'RPC' protocols and file formats.  Additional documentation
 is available in two included vignettes one of which corresponds to our 'JSS'

%package lib
Summary: lib components for the R-RProtoBuf package.
Group: Libraries

%description lib
lib components for the R-RProtoBuf package.


%prep
%setup -q -c -n RProtoBuf
cd %{_builddir}/RProtoBuf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589525353

%install
export SOURCE_DATE_EPOCH=1589525353
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RProtoBuf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RProtoBuf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RProtoBuf
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RProtoBuf || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RProtoBuf/CITATION
/usr/lib64/R/library/RProtoBuf/DESCRIPTION
/usr/lib64/R/library/RProtoBuf/INDEX
/usr/lib64/R/library/RProtoBuf/Meta/Rd.rds
/usr/lib64/R/library/RProtoBuf/Meta/demo.rds
/usr/lib64/R/library/RProtoBuf/Meta/features.rds
/usr/lib64/R/library/RProtoBuf/Meta/hsearch.rds
/usr/lib64/R/library/RProtoBuf/Meta/links.rds
/usr/lib64/R/library/RProtoBuf/Meta/nsInfo.rds
/usr/lib64/R/library/RProtoBuf/Meta/package.rds
/usr/lib64/R/library/RProtoBuf/Meta/vignette.rds
/usr/lib64/R/library/RProtoBuf/NAMESPACE
/usr/lib64/R/library/RProtoBuf/NEWS.Rd
/usr/lib64/R/library/RProtoBuf/R/RProtoBuf
/usr/lib64/R/library/RProtoBuf/R/RProtoBuf.rdb
/usr/lib64/R/library/RProtoBuf/R/RProtoBuf.rdx
/usr/lib64/R/library/RProtoBuf/THANKS
/usr/lib64/R/library/RProtoBuf/demo/addressbook.R
/usr/lib64/R/library/RProtoBuf/demo/io.R
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-intro.Rnw
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-intro.pdf
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-paper.Rnw
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-paper.pdf
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-quickref.Rnw
/usr/lib64/R/library/RProtoBuf/doc/RProtoBuf-quickref.pdf
/usr/lib64/R/library/RProtoBuf/doc/index.html
/usr/lib64/R/library/RProtoBuf/examples/addressbook.pb
/usr/lib64/R/library/RProtoBuf/help/AnIndex
/usr/lib64/R/library/RProtoBuf/help/RProtoBuf.rdb
/usr/lib64/R/library/RProtoBuf/help/RProtoBuf.rdx
/usr/lib64/R/library/RProtoBuf/help/aliases.rds
/usr/lib64/R/library/RProtoBuf/help/paths.rds
/usr/lib64/R/library/RProtoBuf/html/00Index.html
/usr/lib64/R/library/RProtoBuf/html/R.css
/usr/lib64/R/library/RProtoBuf/opencpu/ocpu-getdata.R
/usr/lib64/R/library/RProtoBuf/opencpu/ocpu-getdata.py
/usr/lib64/R/library/RProtoBuf/opencpu/ocpu-rpc.R
/usr/lib64/R/library/RProtoBuf/opencpu/ocpu-rpc.py
/usr/lib64/R/library/RProtoBuf/opencpu/readme.txt
/usr/lib64/R/library/RProtoBuf/opencpu/rexp_pb2.py
/usr/lib64/R/library/RProtoBuf/proto/addressbook.proto
/usr/lib64/R/library/RProtoBuf/proto/helloworld.proto
/usr/lib64/R/library/RProtoBuf/proto/rexp.proto
/usr/lib64/R/library/RProtoBuf/python/readmsg.py
/usr/lib64/R/library/RProtoBuf/python/runtest.sh
/usr/lib64/R/library/RProtoBuf/python/writemsg.R
/usr/lib64/R/library/RProtoBuf/tests/tinytest.R
/usr/lib64/R/library/RProtoBuf/tinytest/data/bytes.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/cyclical/proj1/proto/a.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/cyclical/proj1/proto/c.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/cyclical/proj2/proto/b.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/encoding.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/int64.ascii
/usr/lib64/R/library/RProtoBuf/tinytest/data/nested.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/proto3.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/recursive/subdir/subdir_message.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/subdir/subdir_message.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/unittest.proto
/usr/lib64/R/library/RProtoBuf/tinytest/data/unittest_import.proto
/usr/lib64/R/library/RProtoBuf/tinytest/test_addressbook.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_bool.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_bytes.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_descriptors.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_enums.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_extensions.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_extremevalues.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_fielddescriptor.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_golden_message.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_import.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_int32.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_int64.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_messages.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_nested.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_proto3.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_serialize.R
/usr/lib64/R/library/RProtoBuf/tinytest/test_serialize_pb.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RProtoBuf/libs/RProtoBuf.so
