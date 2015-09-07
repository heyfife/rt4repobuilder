Name:           perl-Class-Container
Version:        0.12
#Release:        9%{?dist}
Release:        0.9%{?dist}
Summary:        Class::Container Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Container/
Source0:        http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate) >= 0.23
Requires:       perl(Params::Validate) >= 0.23
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and
several other objects must create each other transparently, passing the
appropriate parameters to the right class, possibly substituting other
subclasses for any of these objects.

The main features of "Class::Container" are:

*   Explicit declaration of containment relationships (aggregation,
    factory creation, etc.)

*   Declaration of constructor parameters accepted by each member in a
    class framework

*   Transparent passing of constructor parameters to the class that
    needs them

*   Ability to create one (automatic) or many (manual) contained objects
    automatically and transparently

%prep
%setup -q -n Class-Container-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

perldoc -t perlgpl > COPYING
perldoc -t perlartistic > Artistic

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README COPYING Artistic
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.12-0.9
- Port to RHEL 7, use lower release number to avoid upstream conflict

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.12-7
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.12-6
- rebuild for new perl

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.12-5
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.12-4
- Canonicalize Source0 URL.
- Fix find option order.

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 0.12-3
- Remove explicit core module dependencies
- Add COPYING and Artistic

* Wed Aug 17 2005 Steven Pritchard <steve@kspei.com> 0.12-2
- Minor spec cleanup

* Tue Aug 16 2005 Steven Pritchard <steve@kspei.com> 0.12-1
- Specfile autogenerated.