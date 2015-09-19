Name:           perl-Test-HTTP-Server-Simple
Version:        0.11
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Test::More functions for HTTP::Server::Simple
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-HTTP-Server-Simple/

Source0:        http://www.cpan.org/authors/id/A/AL/ALEXMV/Test-HTTP-Server-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More)

# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This mixin class provides methods to test an HTTP::Server::Simple-based web
server. Currently, it provides only one such method: started_ok.

%prep
%setup -q -n Test-HTTP-Server-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.11-0.1
- Port to RHEL 7, roll back release to avoid upstream dependency.

* Mon Nov 23 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.11-1
- Upstream update.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10-1
- Upstream update.
- Reflect upstream maintainer having changed.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-3
- BR: perl(Test::Pod), perl(Test::Pod::Coverage).

* Mon Sep 22 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-2
- Adjust License-tag.

* Mon Sep 22 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Remove bogus R: generated by cpanspec.
- Specfile autogenerated by cpanspec 1.77.
