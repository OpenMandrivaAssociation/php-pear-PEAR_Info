%define		_class		PEAR
%define		_subclass	Info
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.9.2
Release:	7
Summary:	Show Information about your PEAR install and its packages
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PEAR_Info/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package generates a comprehensive information page for your
current PEAR install.
- The format for the page is similar to that for phpinfo() except
  using PEAR colors.
- Has complete PEAR Credits (based on the packages you have
  installed).
- Will show if there is a newer version than the one presently
  installed (and what its state is).
- Each package has an anchor in the form pkg_PackageName - where
  PackageName is a case-sensitive PEAR package name.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_bindir}/pearinfo
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-6mdv2012.0
+ Revision: 742177
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-5
+ Revision: 679556
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-4mdv2011.0
+ Revision: 613749
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.2-3mdv2010.1
+ Revision: 467947
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.9.2-2mdv2010.0
+ Revision: 441505
- rebuild

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.2-1mdv2009.1
+ Revision: 357912
- update to new version 1.9.2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-2mdv2009.1
+ Revision: 322561
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-1mdv2009.1
+ Revision: 305812
- update to new version 1.9.0

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.0-1mdv2009.1
+ Revision: 292888
- update to new version 1.8.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-2mdv2009.0
+ Revision: 237043
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-1mdv2007.0
+ Revision: 82503
- Import php-pear-PEAR_Info

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-1mdk
- 1.6.1

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdk
- initial Mandriva package (PLD import)

