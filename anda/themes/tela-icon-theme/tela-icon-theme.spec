%global tag 2024-09-04

Name:           tela-icon-theme
Version:        20240904
Release:        1%?dist
Summary:        Tela icon theme for linux desktops

License:        GPL-3.0
URL:            https://github.com/vinceliuice/Tela-icon-theme/
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  gtk-update-icon-cache fdupes

%description
Tela icon theme for linux desktops.

%prep
%autosetup -n Tela-icon-theme-%{tag}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -c -d %{buildroot}%{_datadir}/icons

%fdupes %buildroot%_datadir/icons/

%files
%license COPYING
%doc README.md

%{_datadir}/icons/Tela*/

%changelog
%autochangelog
