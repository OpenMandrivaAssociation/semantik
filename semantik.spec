Name:	                semantik
Summary:	        Mindmapping-like tool
Version:		0.6.0
Release:		%mkrel 1
Epoch:			1
Group:		        Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
Patch0:			semantik-0.6.0-kde4-config.patch
BuildRoot:	        %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:		kdegames4-devel kdebase4-devel qt4-linguist
BuildRequires:          libxml2-utils 
BuildRequires:          desktop-file-utils
BuildRequires:		imagemagick
BuildRequires:		ocaml
%py_requires -d
Obsoletes:		kdissert
Provides:		kdissert

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help
students to produce complicated documents very quickly and efficiently:
presentations, dissertations, thesis, reports. While targetted mostly
at students, Kdissert can also help teachers, decision maker, engineers
and businessmen. Semantik is also available exclusively for Linux and
other free operating systems.

%post
%update_menus
%update_icon_cache hicolor
/sbin/ldconfig

%postun
%clean_menus
%clean_icon_cache hicolor
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE.QPL
%{_bindir}/%{name}
%{_libdir}/libnablah.so

%{_datadir}/%{name}

%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0 -b  .orig

%build
./waf configure --qtdir=%{qt4dir} --qtincludes=%{qt4include} \
	--qtlibs=%{qt4lib} --qtbin=%{qt4dir}/bin \
	--prefix=%{_prefix} --icons=%{_iconsdir} \
%if "%{_lib}" != "lib"
	--use64
%endif

./waf build

%install
./waf install --destdir=%buildroot

#icons
install -D -m644 src/data/hi48-app-semantik.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D -m644 src/data/hi64-app-semantik.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D -m644 src/data/hi22-app-semantik.png %{buildroot}%{_iconsdir}/hicolor/22x22/apps/%{name}.png

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{32x32,16x16}/apps
convert -resize 32x32 src/data/hi64-app-semantik.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -resize 16x16 src/data/hi64-app-semantik.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# Menu Entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Presentation" \
  --dir $RPM_BUILD_ROOT%_datadir/applications/ $RPM_BUILD_ROOT%_datadir/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT
