# Maintainer: Danil Osherov <shindo@yandex-team.ru>

tar czf rapidjson.tar.gz rapidjson/

pkgname=librapidjson
pkgver=1.0.2
pkgrel=1
pkgdesc="A fast JSON parser/generator for C++ with both SAX/DOM style API"
arch=('any')
url=('https://github.com/miloyip/rapidjson/')
license=('MIT')
makedepends=('git' 'cmake' 'doxygen')
checkdepends=('valgrind')
source=("rapidjson.tar.gz")
md5sums=('SKIP')

build() {
	cd "$srcdir/rapidjson"
	cmake \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DRAPIDJSON_BUILD_EXAMPLES=OFF \
		-DRAPIDJSON_BUILD_THIRDPARTY_GTEST=ON \
		-DRAPIDJSON_HAS_STDSTRING=ON \
		-DCMAKE_CXX_FLAGS=-mno-avx
	make -j $(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 1)
}

check() {
	cd "$srcdir/rapidjson"
	ctest -V
}

package() {
	cd "$srcdir/rapidjson"

	make DESTDIR="${pkgdir}/" install
	install -D -m644 license.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
