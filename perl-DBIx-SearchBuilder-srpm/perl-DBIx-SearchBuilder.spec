Name:           perl-DBIx-SearchBuilder
Version:        1.67
Release:        1%{?dist}
Summary:        Encapsulate SQL queries and rows in simple perl objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-SearchBuilder/
Source0:        http://www.cpan.org/authors/id/B/BP/BPS/DBIx-SearchBuilder-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::AutoInstall)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires:  perl(capitalization) >= 0.03
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::ReturnValue) >= 0.4
BuildRequires:  perl(Clone)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::DBSchema)
BuildRequires:  perl(Encode) >= 1.99
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.52
BuildRequires:  perl(Want)
Requires:       perl(Cache::Simple::TimedExpiry) >= 0.21
Requires:       perl(capitalization) >= 0.03
Requires:       perl(Class::Accessor)
Requires:       perl(Class::ReturnValue) >= 0.4
Requires:       perl(Clone)
Requires:       perl(DBI)
Requires:       perl(DBIx::DBSchema)
Requires:       perl(Encode) >= 1.99
Requires:       perl(Scalar::Util)
Requires:       perl(Want)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an object-oriented mechanism for retrieving and
updating data in a DBI-accesible database.

%prep
%setup -q -n DBIx-SearchBuilder-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
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
%doc Changes README ROADMAP
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%exclude %{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*
%changelog
* Mon Aug 07 2017 Edward Croasdell <edward.croasdell@sky.uk> 1.67-1
- Specfile autogenerated by cpanspec 1.78.
