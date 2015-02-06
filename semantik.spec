Summary:	Mindmapping-like tool
Name:		semantik
Version:	0.8.4
Release:	2
Epoch:		1
License:	GPLv3+
Group:		Office
Url:		http://code.google.com/p/semantik/
Source0:	http://semantik.googlecode.com/files/semantik-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
BuildRequires:	imagemagick
BuildRequires:	libxml2-utils
BuildRequires:	python-kde4
BuildRequires:	waf
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(python)
Requires:	kdebase4-runtime
Requires:	python-kde4

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help
students to produce complicated documents very quickly and efficiently:
presentations, dissertations, thesis, reports. While targetted mostly
at students, Kdissert can also help teachers, decision maker, engineers
and businessmen. Semantik is also available exclusively for Linux and
other free operating systems.

%files -f %{name}.lang
%doc README
%{_kde_bindir}/%{name}
%{_kde_libdir}/libnablah.so
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
waf configure \
	--qtdir=%{qt4dir} \
	--qtlibs=%{qt4lib} \
	--qtbin=%{qt4dir}/bin \
	--prefix=%{_kde_prefix} \
	--icons=%{_kde_iconsdir} \
%if "%{_lib}" != "lib"
	--use64
%endif

waf build --verbose

%install
waf install --destdir=%{buildroot}

%find_lang %{name}
