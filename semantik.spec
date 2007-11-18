Name:	                semantik
Summary:	        Mindmapping-like tool
Version:		0.6.0
Release:		%mkrel 1
Epoch:			1
Group:		        Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
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
%{_kde_bindir}/%{name}
%{_kde_libdir}/libnablah.so
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

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

./waf build %(echo %_smp_mflags|sed -e 's/j/j /')

%install
./waf install --destdir=%buildroot

# Menu Entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Presentation" \
  --dir $RPM_BUILD_ROOT%_kde_datadir/applications/kde4/ $RPM_BUILD_ROOT%_kde_datadir/applications/kde4/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT
