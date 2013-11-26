Name:           perl-RT-Extension-MandatoryFields
Version:        0.6
Release:        0.1%{?dist}
Summary:        Enforce users to fill standard fields when creating a ticket
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/RT-Extension-MandatoryFields/
Source0:        http://www.cpan.org/modules/by-module/RT/RT-Extension-MandatoryFields-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(rt) >= 4.0.0
Requires:       perl(rt) >= 4.0.0
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This RT Extension enforces users to fill standard fields defined in RT site
configuration file when creating a ticket via the web interface. Filling
can be enforced on tickets created in specified queues only.

%prep
%setup -q -n RT-Extension-MandatoryFields-%{version}

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
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 26 2013 "Nico Kadel-Garcia <nkadel@gmail.com>" 0.6-1
- Specfile autogenerated by cpanspec 1.78.
