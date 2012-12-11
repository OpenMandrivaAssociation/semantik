Name:	        semantik
Summary:	    Mindmapping-like tool
Version:		0.7.3
Release:		3
Epoch:			1
Group:		    Office
License:		QPLv1
URL:			http://freehackers.org/~tnagy/semantik.html
Source0:		http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
Patch0:			semantik-0.6.4-fix-desktop.patch
Patch1:			build_against_new_ocaml.patch
BuildRequires:  kdelibs4-devel
BuildRequires:  libxml2-utils 
BuildRequires:	imagemagick
BuildRequires:	ocaml
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

%files
%defattr(-,root,root)
%doc README
%{_kde_bindir}/%{name}
%{_kde_libdir}/libnablah.so
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
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

%clean


%changelog
* Wed Feb 23 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1:0.7.3-2mdv2011.0
+ Revision: 639476
- Patched to build against new ocaml versions

* Mon Aug 31 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:0.7.3-1mdv2010.0
+ Revision: 422742
- New version 0.7.3

* Sat Jul 11 2009 Funda Wang <fwang@mandriva.org> 1:0.7.2-2mdv2010.0
+ Revision: 394814
- use shipped waf

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Fix release
    - Remove old macros

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1:0.7.2-1mdv2010.0
+ Revision: 369440
- New version 0.7.2

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1:0.6.9-1mdv2009.1
+ Revision: 320338
- simplify BR
- use flags
- drop wrongly installed locale files

  + Adam Williamson <awilliamson@mandriva.org>
    - new release 0.6.9

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:0.6.8-2mdv2009.0
+ Revision: 269246
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 07 2008 Funda Wang <fwang@mandriva.org> 1:0.6.8-1mdv2009.0
+ Revision: 202732
- kdegames are not needed
- New version 0.6.8

* Sun Jan 06 2008 Funda Wang <fwang@mandriva.org> 1:0.6.4-2mdv2008.1
+ Revision: 145924
- add non-KDE4 DE wrapper

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Funda Wang <fwang@mandriva.org> 1:0.6.4-1mdv2008.1
+ Revision: 114054
- New version 0.6.4
- use parallel build
- conver to kde4 style
- use kde4 dirs
- BR kdebase4 and kdegames4
- patch kde4.py too
- add kde4-config patch
- BR kdelibs4
- New version 0.6.0

* Tue Oct 09 2007 Funda Wang <fwang@mandriva.org> 1:0.5.8-1mdv2008.1
+ Revision: 95898
- New version 0.5.8

* Thu Aug 30 2007 Funda Wang <fwang@mandriva.org> 1:0.5.3b-1mdv2008.0
+ Revision: 75150
- New version 0.5.3b

* Thu Aug 30 2007 Funda Wang <fwang@mandriva.org> 1:0.5.3a-1mdv2008.0
+ Revision: 75061
- BR qt4-linguist
- drop BR of kdelibs-devel (icons already specified on configure script)
- New version 0.5.3a
- Don't support libsuffix any more
- it required kde-config to install icons??
- fix upgrading from kdissert
- use hicolor icon theme
- clean up file list
- more fix for waf script
- New version 0.5.3
- kdissert renamed to semantik

* Tue Jun 26 2007 Funda Wang <fwang@mandriva.org> 1.0.7-2mdv2008.0
+ Revision: 44388
- fix file list
- fix desktop category

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Remove X-MandrivaLinux-* keywords
    - Drop old menu style && fix compilation
    - New version


* Sun Jul 02 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-4mdv2007.0
- Rebuild for new menu and extension
- Use macros for icons

* Wed May 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-3mdk
- Rebuild to generate categories

* Mon Oct 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-2mdk
- Add missing icons

* Mon Oct 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-1mdk
- New release 1.0.5
	- new inline editor (hit the keys 'e', 'a', or 'i' to raise it)
	- auto-sizing canvas
	- generate documents from the command-line 
	- minor bugfixes

* Thu Oct 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-0.1mdk
- 1.0.5 => svn snapshot
- cosmetics

* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.4-2mdk
- Fix Requires/BuildRequires

* Mon Aug 08 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.4-1mdk
- New release 1.0.4

* Wed Jul 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3.5-2mdk
- Fix Build for lib64

* Wed Jul 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3.5-1mdk
- 1.0.3.5
         - Bugfixes

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3.2-3mdk
- disable rpath

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3.2-2mdk
- Fix build on x86_64

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3.2-1mdk
- 1.0.3.2

* Tue Jul 19 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3-1mdk
- First Mandriva Package

