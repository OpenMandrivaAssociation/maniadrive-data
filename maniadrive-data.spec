%define game_name maniadrive
%define name %{game_name}-data
%define version 1.2
%define distname ManiaDrive-%{version}-data

%define release 5

Summary: ManiaDrive data files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.gz
License: GPL
Group: Games/Arcade
Url: https://maniadrive.raydium.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
ManiaDrive data files

%prep
%setup -q -n %{distname}
pushd game
    ls *.mni > mania_server_tracks.txt
popd

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}
cp -a game %{buildroot}%{_gamesdatadir}/%{game_name}
rm -f %{buildroot}%{_gamesdatadir}/%{game_name}/php.ini
rm -f %{buildroot}%{_gamesdatadir}/%{game_name}/*.php
rm -rf %{buildroot}%{_gamesdatadir}/%{game_name}/rayphp
find %{buildroot}%{_gamesdatadir}/%{game_name} -type d -exec chmod 755 {} \;
find %{buildroot}%{_gamesdatadir}/%{game_name} -type f -exec chmod 644 {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_gamesdatadir}/%{game_name}




%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-4mdv2011.0
+ Revision: 612813
- the mass rebuild of 2010.1 packages

* Tue Apr 27 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2-3mdv2010.1
+ Revision: 539391
- CCBUG: 58861
- Rebuild package to not provide a bogus php.ini, and provide maps file for mania_sever.

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2-2mdv2010.0
+ Revision: 439745
- rebuild

* Wed Feb 11 2009 Emmanuel Andry <eandry@mandriva.org> 1.2-1mdv2009.1
+ Revision: 339609
- New version 1.2

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.01-5mdv2009.0
+ Revision: 251853
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.01-3mdv2008.1
+ Revision: 140944
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Sep 03 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-03 12:28:22 (59662)
- don't package php files

* Sat Sep 02 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-02 21:42:30 (59633)
- don't package rayphp files anymore

* Mon Aug 21 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-21 13:57:43 (56970)
- initial Mandriva release

* Mon Aug 21 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-21 13:53:45 (56965)
- Created package structure for maniadrive-data.

