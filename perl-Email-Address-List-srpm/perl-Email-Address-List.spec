Name:           perl-Email-Address-List
Version:        0.05
Release:        1%{?dist}
Summary:        RFC close address list parsing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Email-Address-List/
Source0:        http://www.cpan.org/authors/id/A/AL/ALEXMV/Email-Address-List-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.10.0
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::More)
Requires:       perl(Email::Address)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Parser for From, To, Cc, Bcc, Reply-To, Sender and previous prefixed with
Resent- (eg Resent-From) headers.

%prep
%setup -q -n Email-Address-List-%{version}

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
* Fri Aug 04 2017 Ryan Fife <ryan@fife-v.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
