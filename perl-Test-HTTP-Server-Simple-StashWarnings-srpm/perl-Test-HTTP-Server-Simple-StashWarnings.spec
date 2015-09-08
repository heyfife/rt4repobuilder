Name:           perl-Test-HTTP-Server-Simple-StashWarnings
Version:        0.04
Release:        2%{?dist}
Summary:        Catch your forked server's warnings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-HTTP-Server-Simple-StashWarnings/
Source0:        http://www.cpan.org/authors/id/J/JE/JESSE/Test-HTTP-Server-Simple-StashWarnings-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.34
BuildRequires:  perl(Test::HTTP::Server::Simple)
BuildRequires:  perl(WWW::Mechanize)
Requires:       perl(Test::HTTP::Server::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Warnings are an important part of any application. Your web application
should warn the user when something is amiss.

%prep
%setup -q -n Test-HTTP-Server-Simple-StashWarnings-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ralf Corsépius corsepiu@fedoraproject.org> - 0.04-1
- Upstream update.
- Change Source0-URL to reflect upstream maintainer change.
- Disallow testsuite to fail.

* Tue Apr 21 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.03-3
- Allow testsuite to fail.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Specfile autogenerated by cpanspec 1.77.
