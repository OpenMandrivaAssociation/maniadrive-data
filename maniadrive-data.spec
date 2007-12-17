%define game_name maniadrive
%define name %{game_name}-data
%define version 1.01
%define distname ManiaDrive-%{version}-data

%define release %mkrel 3

Summary: ManiaDrive data files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: Games/Arcade
Url: http://maniadrive.raydium.org/
BuildArch: noarch


%description
ManiaDrive data files

%prep
%setup -q -n %{distname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamesdatadir}
cp -a game $RPM_BUILD_ROOT%{_gamesdatadir}/%{game_name}
rm -f $RPM_BUILD_ROOT%{_gamesdatadir}/%{game_name}/*.php
rm -rf $RPM_BUILD_ROOT%{_gamesdatadir}/%{game_name}/rayphp
find $RPM_BUILD_ROOT%{_gamesdatadir}/%{game_name} -type d -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{_gamesdatadir}/%{game_name} -type f -exec chmod 644 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%{_gamesdatadir}/%{game_name}


