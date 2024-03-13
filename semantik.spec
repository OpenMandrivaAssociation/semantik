%define _disable_lto 1
%define _disable_ld_no_undefined 1

Summary:	Mindmapping-like tool
Name:		semantik
Version:	1.2.11
Release:	1
Epoch:		1
License:	GPLv3+
Group:		Office
Url:		http://waf.io/semantik/
Source0:	https://waf.io/semantik-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
BuildRequires:	imagemagick
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(python3)
BuildRequires:	python2
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:  cmake(KF5SonnetUi)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help
students to produce complicated documents very quickly and efficiently:
presentations, dissertations, thesis, reports. While targetted mostly
at students, Kdissert can also help teachers, decision maker, engineers
and businessmen. Semantik is also available exclusively for Linux and
other free operating systems.

%files -f %{name}.lang
%doc README
%{_kde5_bindir}/%{name}
%{_kde5_bindir}/%{name}-d
%{_kde5_libdir}/libsemantik.so*
%{_kde5_datadir}/%{name}
%{_kde5_datadir}/kxmlgui5/semantik*
%{_kde5_datadir}/applications/%{name}*.desktop
%{_kde5_iconsdir}/*/*/*/*
%{_kde5_datadir}/mime/packages/%{name}.xml

#--------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export CXXFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
python2 waf configure \
	--qtdir=%{_libdir}/qt5 \
	--qtlibs=%_qt5_libdir \
	--qtbin=%_qt5_bindir \
	--prefix=%{_kde5_prefix} \
	--icons=%{_kde5_iconsdir} \

python2 waf build --verbose

%install
python2 waf install --destdir=%{buildroot}

#useless .so
rm -f %{buildroot}/%{_kde5_libdir}/libsemantik.so

%find_lang %{name}-d %{name} %{name}.lang
