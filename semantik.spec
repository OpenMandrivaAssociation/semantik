Name:	        semantik
Summary:	    Mindmapping-like tool
Version:		0.7.3
Release:		3
Epoch:			1
Group:		    Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
Source1:		%{name}.rpmlintrc
Patch0:			semantik-0.6.4-fix-desktop.patch
Patch1:			build_against_new_ocaml.patch
BuildRequires:  kdelibs4-devel
BuildRequires:  libxml2-utils 
BuildRequires:	imagemagick
BuildRequires:	python-devel
BuildRequires:	ocaml
Requires:		kdebase4-runtime
Obsoletes:		kdissert
Provides:		kdissert

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help
students to produce complicated documents very quickly and efficiently:
presentations, dissertations, thesis, reports. While targetted mostly
at students, Kdissert can also help teachers, decision maker, engineers
and businessmen. Semantik is also available exclusively for Linux and
other free operating systems.

%files
%doc README
%{_kde_bindir}/%{name}
%{_kde_libdir}/libnablah.so
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .orig
%patch1 -p0

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

./waf build %_smp_mflags --want-rpath=0

%install
./waf install --destdir=%{buildroot}
