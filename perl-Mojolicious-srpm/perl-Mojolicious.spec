Name:           perl-Mojolicious
Version:        5.04
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Real-time web framework
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mojolicious/
Source0:        http://www.cpan.org/authors/id/S/SR/SRI/Mojolicious-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.010001
BuildRequires:  perl(Digent::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Take a look at our excellent documentation in Mojolicious::Guides!

%prep
%setup -q -n Mojolicious-%{version}

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
%doc Changes CONTRIBUTING.md LICENSE META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Jun 07 2014 Nico Kadel-Garcia <nkadel@gmail.com> 5.04-1
- Specfile autogenerated by cpanspec 1.78.
- Added man1/* and bin/* files not found by cpanspec.
