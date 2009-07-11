Name:	                semantik
Summary:	        Mindmapping-like tool
Version:		0.7.2
Release:		%mkrel 
Epoch:			1
Group:		        Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
Patch0:			semantik-0.6.4-fix-desktop.patch
BuildRoot:	        %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:          kdelibs4-devel
BuildRequires:          libxml2-utils 
BuildRequires:		imagemagick
BuildRequires:		ocaml
BuildRequires:		waf
Requires:		kdebase4-runtime
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

%files -f %name.lang
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
%patch0 -p0 -b .orig

%build
export CXXFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
./waf configure \
	--qtdir=%{qt4dir} --qtincludes=%{qt4include} \
	--qtlibs=%{qt4lib} --qtbin=%{qt4dir}/bin \
	--prefix=%_kde_prefix --icons=%_kde_iconsdir \
%if "%{_lib}" != "lib"
	--use64
%endif

%waf

%install
rm -fr %buildroot
%waf_install

#rm -fr %buildroot%_datadir/locale

%find_lang %name

%clean
rm -rf %{buildroot}
