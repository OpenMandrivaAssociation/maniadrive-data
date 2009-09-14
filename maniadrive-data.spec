%define game_name maniadrive
%define name %{game_name}-data
%define version 1.2
%define distname ManiaDrive-%{version}-data

%define release %mkrel 2

Summary: ManiaDrive data files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.gz
License: GPL
Group: Games/Arcade
Url: http://maniadrive.raydium.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
ManiaDrive data files

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}
cp -a game %{buildroot}%{_gamesdatadir}/%{game_name}
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


