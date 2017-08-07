Name:           perl-CSS-Minifier-XS
Version:        0.09
Release:        1%{?dist}
Summary:        XS based CSS minifier
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CSS-Minifier-XS/
Source0:        http://www.cpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
CSS::Minifier::XS is a CSS "minifier"; its designed to remove un-necessary
whitespace and comments from CSS files, while also not breaking the CSS.

%prep
%setup -q -n CSS-Minifier-XS-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CSS*
%{_mandir}/man3/*

%changelog
* Mon Aug 07 2017 Edward Croasdell <edward.croasdell@sky.uk> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
