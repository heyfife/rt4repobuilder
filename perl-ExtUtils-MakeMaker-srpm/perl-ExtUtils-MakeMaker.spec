Name:           perl-ExtUtils-MakeMaker
Version:        7.30
Release:        1%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-MakeMaker/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Pod::Man)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Pod::Man)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%prep
%setup -q -n ExtUtils-MakeMaker-%{version}

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
%doc Changes CONTRIBUTING META.json README README.packaging
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 07 2017 Ryan Fife <ryan@fife-v.com> 7.30-1
- Specfile autogenerated by cpanspec 1.78.
