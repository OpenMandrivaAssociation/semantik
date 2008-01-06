Name:	                semantik
Summary:	        Mindmapping-like tool
Version:		0.6.4
Release:		%mkrel 2
Epoch:			1
Group:		        Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
Patch0:			semantik-0.6.4-fix-desktop.patch
BuildRoot:	        %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:		kdegames4-devel kdebase4-devel qt4-linguist
BuildRequires:          libxml2-utils 
BuildRequires:		imagemagick
BuildRequires:		ocaml
Requires:		kdebase4-workspace
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

%files -f %name.lang
%defattr(-,root,root)
%doc README LICENSE.QPL
%{_kde_bindir}/%{name}
%{_kde_libdir}/libnablah.so
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/applications/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%{_iconsdir}/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0 -b .orig

%build
export PATH=%_kde_bindir:%qt4bin:$PATH
export KDEDIR=%_kde_prefix
export KDEDIRS=%_kde_prefix
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
./waf configure --qtdir=%{qt4dir} --qtincludes=%{qt4include} \
	--qtlibs=%{qt4lib} --qtbin=%{qt4dir}/bin \
	--prefix=%_kde_prefix --icons=%_kde_iconsdir \
%if "%{_lib}" != "lib"
	--use64
%endif

./waf build 

%install
./waf install --destdir=%buildroot

# add wrapper for non-KDE4 DEs
mkdir -p %buildroot%_datadir/applications
mkdir -p %buildroot%_iconsdir
sed -e 's|Exec=semantik|Exec=k4 semantik|' %buildroot%{_kde_datadir}/applications/kde4/%name.desktop > \
	%buildroot%_datadir/applications/%name.desktop
cp -fr %buildroot%_kde_iconsdir/hicolor %buildroot%_iconsdir

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
