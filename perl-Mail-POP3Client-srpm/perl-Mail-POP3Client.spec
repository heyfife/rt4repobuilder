Name:           perl-Mail-POP3Client
Version:        2.18
#Release:        6%{?dist}
Release:        0.6%{?dist}
Summary:        Perl 5 module to talk to a POP3 (RFC1939) server
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mail-POP3Client/
Source0:        http://www.cpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements an Object-Oriented interface to a POP3 server. It
implements RFC1939 (http://www.faqs.org/rfcs/rfc1939.html)

%prep
%setup -q -n Mail-POP3Client-%{version}

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
%doc Changes FAQ README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com< - 2.18-0.6
- Port to RHEL 7, roll back release to avoid upstream repository conflict.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.18-6
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.18-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.18-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 2.18-1
- Specfile autogenerated by cpanspec 1.77.
