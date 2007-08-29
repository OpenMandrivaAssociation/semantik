%define version	        1.0.7
%define release	        %mkrel 2

Name:	                kdissert	        
Summary:	        Mindmapping-like tool 
Version:		%{version}
Release:		%{release}
Group:		        Office
License:		GPL
URL:			http://freehackers.org/~tnagy/kdissert/index.html
Source0:		http://freehackers.org/~tnagy/kdissert/%name-%version.tar.bz2
BuildRoot:	        %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:		kdelibs-devel
BuildRequires:          libxml2-utils 
BuildRequires:          desktop-file-utils
BuildRequires:          python-devel

Requires:               kdebase-progs

%description
kdissert is a mindmapping-like tool to help students to 
produce complicated documents very quickly and efficiently : 
presentations, dissertations, thesis, reports ... The concept 
is innovative : mindmaps produced using kdissert are processed 
to output near-ready-to-use documents. While targetted mostly at 
students, kdissert can also help teachers, decision maker, engineers 
and businessmen.

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/kdissert

%{_iconsdir}/kdissert.png
%{_liconsdir}/kdissert.png
%{_miconsdir}/kdissert.png

%{_datadir}/applnk/Utilities/%{name}.desktop
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_datadir}/services/%{name}part.desktop
%{_datadir}/applications/kde/%{name}.desktop

%dir %{_datadir}/apps/%{name}/
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_datadir}/apps/%{name}/pics/nopix.png
%{_datadir}/apps/%{name}/templatedata/kdissOOOdoc.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissOOOimpress.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissapplet.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissasciidoc.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissbeamerslides.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdisshtmldoc.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdisspdflatexarticle.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdisspdflatexbook.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissprosperslides.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissstx.tar.gz
%{_datadir}/apps/%{name}/templatedata/kdissdocbook.tar.gz
%{_datadir}/apps/%{name}/tips

%dir %{_datadir}/apps/%{name}part/
%{_datadir}/apps/%{name}part/%{name}part.rc

%{_datadir}/config.kcfg/kdissert.kcfg

%{_datadir}/icons/hicolor/128x128/actions/%{name}_sort.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/actions/%{name}_link.png
%{_datadir}/icons/hicolor/16x16/actions/%{name}_point.png
%{_datadir}/icons/hicolor/16x16/actions/%{name}_sort.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/actions/%{name}_link.png
%{_datadir}/icons/hicolor/22x22/actions/%{name}_point.png
%{_datadir}/icons/hicolor/22x22/actions/%{name}_sort.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/actions/%{name}_link.png
%{_datadir}/icons/hicolor/32x32/actions/%{name}_point.png
%{_datadir}/icons/hicolor/32x32/actions/%{name}_sort.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/actions/%{name}_sort.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%{_libdir}/kde3/libkdissOOOdoc.la
%{_libdir}/kde3/libkdissOOOdoc.so
%{_libdir}/kde3/libkdissOOOimpress.la
%{_libdir}/kde3/libkdissOOOimpress.so
%{_libdir}/kde3/libkdissapplet.la
%{_libdir}/kde3/libkdissapplet.so
%{_libdir}/kde3/libkdissasciidoc.la
%{_libdir}/kde3/libkdissasciidoc.so
%{_libdir}/kde3/libkdissbeamerslides.la
%{_libdir}/kde3/libkdissbeamerslides.so
%{_libdir}/kde3/libkdisshtmldoc.la
%{_libdir}/kde3/libkdisshtmldoc.so
%{_libdir}/kde3/libkdisspdflatexarticle.la
%{_libdir}/kde3/libkdisspdflatexarticle.so
%{_libdir}/kde3/libkdisspdflatexbook.la
%{_libdir}/kde3/libkdisspdflatexbook.so
%{_libdir}/kde3/libkdissprosperslides.la
%{_libdir}/kde3/libkdissprosperslides.so
%{_libdir}/kde3/libkdissstx.la
%{_libdir}/kde3/libkdissstx.so
%{_libdir}/kde3/libkdissdocbook.la
%{_libdir}/kde3/libkdissdocbook.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%define __libtoolize /bin/true



%if "%{_lib}" == "lib64"
./waf configure --libsuffix=64
%else
./waf configure
%endif

./waf

DESTDIR=$RPM_BUILD_ROOT ./waf  install

#icons
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
install -m644 src/appdata/hi22-app-kdissert.png $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install -m644 src/appdata/hi32-app-kdissert.png $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m644 src/appdata/hi64-app-kdissert.png $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

# Menu Entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="QT" \
  --add-category="Qt" \
  --add-category="Presentation" \
  --add-category="Office" \
  --dir $RPM_BUILD_ROOT%_datadir/applnk/Utilities $RPM_BUILD_ROOT%_datadir/applnk/Utilities/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

