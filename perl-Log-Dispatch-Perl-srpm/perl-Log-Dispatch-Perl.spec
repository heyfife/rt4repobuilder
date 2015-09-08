Name:           perl-Log-Dispatch-Perl
Version:        0.03
#Release:        5%{?dist}
Release:        0.5%{?dist}
Summary:        Use core Perl functions for logging
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Dispatch-Perl/
Source0:        http://www.cpan.org/authors/id/E/EL/ELIZABETH/Log-Dispatch-Perl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Log::Dispatch) >= 1.16
Requires:       perl(Log::Dispatch) >= 1.16
Requires:	perl(Carp)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The "Log::Dispatch::Perl" module offers a logging alternative using
standard Perl core functions. It allows you to fall back to the common Perl
alternatives for logging, such as "warn" and "cluck". It also adds the
possibility for a logging action to halt the current environment, such as
with "die" and "croak".

%prep
%setup -q -n Log-Dispatch-Perl-%{version}

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
%doc CHANGELOG README TODO VERSION
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.03-0.1
- Port to RHEL 7, roll back release number to avoid upstream conflict

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-2
- Fix License: tag.

* Mon Sep 22 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Add R: perl(Carp).
- Add BR: perl(Test::More).
- Specfile autogenerated by cpanspec 1.77.
