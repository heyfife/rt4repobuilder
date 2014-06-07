Name:           perl-Data-GUID
Version:        0.048
Release:        1%{?dist}
Summary:        Globally unique identifiers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-GUID/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Data-GUID-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Exporter) >= 0.90
BuildRequires:  perl(Sub::Install) >= 0.03
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Data::UUID) >= 1.148
Requires:       perl(Sub::Exporter) >= 0.90
Requires:       perl(Sub::Install) >= 0.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

%prep
%setup -q -n Data-GUID-%{version}

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
%doc Changes dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Nico Kadel-Garcia <nkadel@gmail.com> 0.048-1
- Specfile autogenerated by cpanspec 1.78.
