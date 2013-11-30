Name:           perl-RT-Extension-CommandByMail
Version:        0.16
Release:        0.1%{?dist}
Summary:        Change metadata of ticket via email
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/RT-Extension-CommandByMail/
Source0:        http://www.cpan.org/modules/by-module/RT/RT-Extension-CommandByMail-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.3
# Force installation of RT version 4 components
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Entity) >= 5.420
BuildRequires:  perl(RT) >= 4.0
BuildRequires:  perl(RT::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  rt4 >= 4.0
BuildRequires:  /usr/sbin/rt-mailgate
Requires:       perl(MIME::Entity) >= 5.420
Requires:       perl(RT)
Requires:       perl(UNIVERSAL::require)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This extension allows you to manage tickets via email interface. You may
put commands into the beginning of a mail, and extension will apply
them. See the list of commands in the
RT::Interface::Email::Filter::TakeAction docs.

%prep
%setup -q -n RT-Extension-CommandByMail-%{version}

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
# Do not make test until further notice, requires running RT 4.
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 26 2013 "Nico Kadel-Garcia <nkadel@gmail.com>" 0.16-1
- Specfile autogenerated by cpanspec 1.78.
- Added BuildRequires for perl(RT).
- Disable 'make test' until access to RT_Config.pm can be worked out,
  requires working RT 4.
