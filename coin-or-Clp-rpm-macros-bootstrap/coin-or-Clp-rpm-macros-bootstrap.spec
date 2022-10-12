Name:           coin-or-Clp-rpm-macros-bootstrap
Version:        1.17.6
Release:        1%{?dist}
Summary:        RPM macros for coin-or-Clp
 
License:        Public Domain
URL:            https://github.com/yamaura/copr-opencv
 
BuildArch:      noarch
 
%description
%{summary}.
 
%prep
%autosetup -c -D -T
 
%build
# Nothing to build
 
%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
echo '%_with_bootstrap 1' > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.coin-or-Clp
 
%files
%{_rpmconfigdir}/macros.d/macros.coin-or-Clp
 
%changelog

