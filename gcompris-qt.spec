Summary:	Educational software suite for children aged 2 to 10
Name:		gcompris-qt
Version:	2.0
Release:	1
License:	AGPLv3
Source0:	http://gcompris.net/download/qt/src/%{name}-%{version}.tar.xz
# Source0-md5:	dd3a7e364c19c7d4beea3fbcf7dbf471
URL:		http://gcompris.net
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sensors-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	appstream-glib
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	qt5-linguist
Requires:	Qt5Multimedia
Requires:	Qt5Quick-controls
Requires:	Qt5Quick-graphicaleffects
Requires:	Qt5Svg
Requires:	hicolor-icon-theme
Obsoletes:	gcompris < 15.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCompris-Qt is an educational software suite comprising of numerous
activities for children aged 2 to 10. Some of the activities are game
orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New activities
can be added, and an activity can implement its own game scheme.

This version is a rewrite of GCompris using the QtQuick technology.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake ../ \
	-DQML_BOX2D_MODULE=disabled

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc LICENSES/AGPL-3.0-only.txt LICENSES/GPL-3.0-or-later.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/metainfo/org.kde.gcompris.appdata.xml
%{_desktopdir}/org.kde.gcompris.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_docdir}/HTML/en/gcompris-qt
%dir %{_datadir}/gcompris-qt/translations
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/rcc
%{_datadir}/gcompris-qt/translations/gcompris_en.qm
%lang(az) %{_datadir}/gcompris-qt/translations/gcompris_az.qm
%lang(be) %{_datadir}/gcompris-qt/translations/gcompris_be.qm
%lang(br) %{_datadir}/gcompris-qt/translations/gcompris_br.qm
%lang(ca) %{_datadir}/gcompris-qt/translations/gcompris_ca.qm
%lang(ca@valencia) %{_datadir}/gcompris-qt/translations/gcompris_ca@valencia.qm
%lang(de) %{_datadir}/gcompris-qt/translations/gcompris_de.qm
%lang(el) %{_datadir}/gcompris-qt/translations/gcompris_el.qm
%lang(en_GB) %{_datadir}/gcompris-qt/translations/gcompris_en_GB.qm
%lang(es) %{_datadir}/gcompris-qt/translations/gcompris_es.qm
%lang(et) %{_datadir}/gcompris-qt/translations/gcompris_et.qm
%lang(eu) %{_datadir}/gcompris-qt/translations/gcompris_eu.qm
%lang(fi) %{_datadir}/gcompris-qt/translations/gcompris_fi.qm
%lang(fr) %{_datadir}/gcompris-qt/translations/gcompris_fr.qm
%lang(he) %{_datadir}/gcompris-qt/translations/gcompris_he.qm
%lang(hu) %{_datadir}/gcompris-qt/translations/gcompris_hu.qm
%lang(id) %{_datadir}/gcompris-qt/translations/gcompris_id.qm
%lang(it) %{_datadir}/gcompris-qt/translations/gcompris_it.qm
%lang(lt) %{_datadir}/gcompris-qt/translations/gcompris_lt.qm
%lang(mk) %{_datadir}/gcompris-qt/translations/gcompris_mk.qm
%lang(ml) %{_datadir}/gcompris-qt/translations/gcompris_ml.qm
%lang(nl) %{_datadir}/gcompris-qt/translations/gcompris_nl.qm
%lang(nn) %{_datadir}/gcompris-qt/translations/gcompris_nn.qm
%lang(pl) %{_datadir}/gcompris-qt/translations/gcompris_pl.qm
%lang(pt) %{_datadir}/gcompris-qt/translations/gcompris_pt.qm
%lang(pt_BR) %{_datadir}/gcompris-qt/translations/gcompris_pt_BR.qm
%lang(ro) %{_datadir}/gcompris-qt/translations/gcompris_ro.qm
%lang(ru) %{_datadir}/gcompris-qt/translations/gcompris_ru.qm
%lang(sl) %{_datadir}/gcompris-qt/translations/gcompris_sl.qm
%lang(sq) %{_datadir}/gcompris-qt/translations/gcompris_sq.qm
%lang(sv) %{_datadir}/gcompris-qt/translations/gcompris_sv.qm
%lang(tr) %{_datadir}/gcompris-qt/translations/gcompris_tr.qm
%lang(uk) %{_datadir}/gcompris-qt/translations/gcompris_uk.qm
%lang(zh_TW) %{_datadir}/gcompris-qt/translations/gcompris_zh_TW.qm
