Name: hunspell-ss
Summary: Swati hunspell dictionaries
%define upstreamid 20060705
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://downloads.translate.org.za/spellchecker/swati/myspell-ss_ZA-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Swati hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ss

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ss_ZA.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060705-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060705-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060705-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060705-1
- initial version
