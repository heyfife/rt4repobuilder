Name:           perl-IO-Socket-IP
Version:        0.39
Release:        1%{?dist}
Summary:        Family-neutral IP socket supporting both IPv4 and IPv6
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Socket-IP/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket) >= 1.97
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Socket) >= 1.97
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, intended as a replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way. For a
list of known differences, see the IO::Socket::INET INCOMPATIBILITES
section below.

%prep
%setup -q -n IO-Socket-IP-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes examples LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 07 2017 Edward Croasdell <edward.croasdell@sky.uk> 0.39-1
- Specfile autogenerated by cpanspec 1.78.
