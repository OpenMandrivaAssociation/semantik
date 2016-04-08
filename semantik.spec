%define _disable_lto 1
%define _disable_ld_no_undefined 1

Summary:	Mindmapping-like tool
Name:		semantik
Version:	0.9.4
Release:	2
Epoch:		1
License:	GPLv3+
Group:		Office
Url:		http://ita1024.github.io/semantik/
Source0:	https://github.com/ita1024/semantik/archive/semantik-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	imagemagick
BuildRequires:	libxml2-utils
BuildRequires:	waf
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(python)
Requires:	kdebase4-runtime
Requires:	python-qt4

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
%{_kde_bindir}/%{name}-d
%{_kde_libdir}/libsemantik.so*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/mime/packages/%{name}.xml

#--------------------------------------------------------------------

%prep
%setup -qn %{name}-%{name}-%{version}

%build
export CXXFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
python2 waf configure \
	--qtdir=%{qt4dir} \
	--qtlibs=%{qt4lib} \
	--qtbin=%{qt4dir}/bin \
	--prefix=%{_kde_prefix} \
	--icons=%{_kde_iconsdir} \

python2 waf build --verbose

%install
python2 waf install --destdir=%{buildroot}

%find_lang %{name}
