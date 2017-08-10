#
# Makefile - build wrapper for Rt 4 on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/rt4repo

# Base directory for yum repository
REPOBASEDIR="`/bin/pwd`"
#REPOBASEDIR="/var/www/html/yum"
# Base subdirectories for RPM deployment
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/7/SRPMS
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/7/x86_64

MFLAGS="--debug=a"

# These build with normal mock "epel-*" setups
EPELPKGS+=google-droid-sans-fonts-srpm
EPELPKGS+=perl-Apache-Session-srpm
EPELPKGS+=perl-CGI-PSGI-srpm
EPELPKGS+=perl-CSS-Minifier-srpm
EPELPKGS+=perl-Cache-Simple-TimedExpiry-srpm
EPELPKGS+=perl-Calendar-Simple-srpm
EPELPKGS+=perl-Capture-Tiny-srpm
EPELPKGS+=perl-Carp-Assert-More-srpm
EPELPKGS+=perl-Class-Container-srpm
EPELPKGS+=perl-CSS-Minifier-XS-srpm
EPELPKGS+=perl-Data-Page-srpm
EPELPKGS+=perl-DBIx-DBschema-srpm
EPELPKGS+=perl-Expect-Simple-srpm
EPELPKGS+=perl-Email-Address-srpm
EPELPKGS+=perl-Email-Address-List-srpm
EPELPKGS+=perl-Encode-srpm
EPELPKGS+=perl-ExtUtils-Installed-srpm
EPELPKGS+=perl-ExtUtils-MakeMaker-srpm
EPELPKGS+=perl-EV-srpm
EPELPKGS+=perl-GnuPG-Interface-srpm
EPELPKGS+=perl-HTML-FormatText-WithLinks-AndTables-srpm
EPELPKGS+=perl-JavaScript-Minifier-XS-srpm
EPELPKGS+=perl-IO-Socket-IP-srpm
EPELPKGS+=perl-List-UtilsBy-srpm
EPELPKGS+=perl-Locale-Maketext-Fuzzy-srpm
EPELPKGS+=perl-Locale-Maketext-Lexicon-srpm
EPELPKGS+=perl-Log-Any-srpm
EPELPKGS+=perl-Log-Dispatch-Perl-srpm
EPELPKGS+=perl-Module-Util-srpm
EPELPKGS+=perl-PerlIO-eol-srpm
EPELPKGS+=perl-Proc-Wait3-srpm
EPELPKGS+=perl-Regexp-Common-Net-CIDR-srpm
EPELPKGS+=perl-Role-Basic-srpm
EPELPKGS+=perl-Scope-Upper-srpm
EPELPKGS+=perl-Set-IntSpan-srpm
EPELPKGS+=perl-Set-Tiny-srpm
EPELPKGS+=perl-Symbol-Global-Name-srpm
EPELPKGS+=perl-Test-Exception-srpm
EPELPKGS+=perl-Test-HTTP-Server-Simple-srpm
EPELPKGS+=perl-Text-Password-Pronounceable-srpm
EPELPKGS+=perl-Text-Quoted-srpm
EPELPKGS+=perl-Text-WikiFormat-srpm
EPELPKGS+=perl-Text-Wrapper-srpm
EPELPKGS+=perl-Tree-Simple-srpm
EPELPKGS+=perl-capitalization-srpm

# Require customized rt4repo local repository for dependencies
# Needed by various packages

# requires perl-Set-IntSpan
RT4PKGS+=perl-Business-Hours-srpm

# Now requires perl-Cache-Simple-TimedExpiry-srpm
RT4PKGS+=perl-DBIx-SearchBuilder-srpm

RT4PKGS+=perl-Test-WWW-Mechanize-srpm

RT4PKGS+=perl-Convert-Color-srpm

RT4PKGS+=perl-GD-Graph-srpm

# Dependency for perl-HTML-Mason-PSGIHandler-srpm
RT4PKGS+=perl-HTML-Mason-srpm
RT4PKGS+=perl-HTML-Mason-PSGIHandler-srpm

RT4PKGS+=perl-HTML-Quoted-srpm
RT4PKGS+=perl-HTML-RewriteAttributes-srpm

RT4PKGS+=perl-HTTP-Server-Simple-Mason-srpm

# Dependency for perl-Parallel-Prefork-srpm
RT4PKGS+=perl-Parallel-Scoreboard-srpm
RT4PKGS+=perl-Parallel-Prefork-srpm

RT4PKGS+=perl-Server-Starter-srpm
RT4PKGS+=perl-Starlet-srpm

RT4PKGS+=perl-Test-Expert-srpm

RT4PKGS+=perl-Test-HTTP-Server-Simple-StashWarnings-srpm

# Needed for rt4-Test building
RT4PKGS+=perl-Test-WWW-Mechanize-PSGI-srpm
RT4PKGS+=perl-Plack-Middleware-Test-StashWarnings-srpm

RT4PKGS+=perl-DateTime-Format-Natural-srpm
RT4PKGS+=perl-Date-Extract-srpm
RT4PKGS+=perl-Data-Page-Pageset-srpm
RT4PKGS+=perl-Data-GUID-srpm
RT4PKGS+=perl-Crypt-X509-srpm

# Dependency for Mojo-DOM
#
RT4PKGS+=perl-Mojolicious-srpm
#RT4PKGS+=perl-IO-Socket-IP-srpm

# Binary target
RT4PKGS+=rt4-srpm

# Add-on utilities, can be compiled with rt3 from EPEL,
# but use rt4 from local builds
#RT4PKGS+=perl-RT-Extension-CommandByMail-srpm
#RT4PKGS+=perl-RT-Extension-MandatoryFields-srpm

# Populate rt4repo with packages compatible with just EPEL
all:: epel-install

# Populate rt4repo with packages that require rt4repo
all:: rt4-install

install:: epel-install rt4-install

rt4repo-7-x86_64.cfg:: rt4repo-7-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

rt4repo-7-x86_64.cfg:: FORCE
	@cmp -s $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

# Used for make build with local components
rt4repo.repo:: rt4repo.repo.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

rt4repo.repo:: FORCE
	@cmp -s $@ /etc/yum.repos.d/$@ || \
		(echo Warning: /etc/yum.repos.d/$@ does not match $@, exiting; exit 1)

epel:: $(EPELPKGS)

$(REPOBASESUBDIRS)::
	mkdir -p $@

epel-install:: $(REPOBASESUBDIRS)

epel-install:: FORCE
	@for name in $(EPELPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

rt4:: $(RT4PKGS)

rt4-install:: FORCE
	@for name in $(RT4PKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

# Dependencies
perl-Convert-Color-srpm:: perl-List-UtilsBy-srpm
perl-DBIx-SearchBuilder-srpm:: perl-Cache-Simple-TimedExpiry-srpm
perl-DBIx-SearchBuilder-srpm:: perl-capitalization-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-HTML-Mason-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Plack-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Test-Log-Dispatch-srpm
perl-HTML-Mason-srpm:: perl-Class-Container-srpm
perl-Mojolicious-srpm:: perl-IO-Socket-IP-srpm
perl-Log-Any-Aapter-srpm:: perl-Log-Any-srpm
perl-Log-Any-Adapter-Dispatch-srpm:: perl-Log-Any-Adapter-srpm
perl-Module-Mask-srpm:: perl-Module-Util-srpm
perl-Parallel-Prefork-srpm:: perl-Class-Accessor-Lite-srpm
perl-Parallel-Prefork-srpm:: perl-Parallel-Scoreboard-srpm
perl-Parallel-Scoreboard-srpm:: perl-Class-Accessor-Lite-srpm
perl-Server-Starter-srpm:: perl-Encode-srpm
perl-Server-Starter-srpm:: perl-Proc-Wait3-srpm
perl-Starlet-srpm:: perl-Parallel-Prefork-srpm
perl-Starlet-srpm:: perl-Server-Starter-srpm
perl-Test-Expert-srpm:: perl-Class-Accessor-Chained-srpm
perl-Test-HTTP-Server-Simple-StashWarnings-srpm:: perl-Test-HTTP-Server-Simple-srpm
perl-Test-WWW-Mechanize-PSGI-srpm:: perl-Test-WWW-Mechanize-srpm
perl-Test-WWW-Mechanize-srpm:: perl-Carp-Assert-More-srpm

rt4:: google-droid-sans-fonts-srpm
rt4:: perl-CGI-PSGI-srpm
rt4:: perl-Calendar-Simple-srpm
rt4:: perl-Convert-Color-srpm
rt4:: perl-DBIx-DBschema-srpm
rt4:: perl-DBIx-SearchBuilder-srpm
rt4:: perl-GnuPG-Interface-srpm
rt4:: perl-HTML-Mason-PSGIHandler-srpm
rt4:: perl-HTML-Mason-srpm
rt4:: perl-HTML-Quoted-srpm
rt4:: perl-HTML-RewriteAttributes-srpm
rt4:: perl-HTTP-Server-Simple-Mason-srpm
rt4:: perl-IO-Socket-IP-srpm
rt4:: perl-Locale-Maketext-Fuzzy-srpm
rt4:: perl-Locale-Maketext-Lexicon-srpm
rt4:: perl-Log-Dispatch-Perl-srpm
rt4:: perl-Mojolicious-srpm
rt4:: perl-Plack-Middleware-Test-StashWarnings-srpm
rt4:: perl-Test-Expert-srpm
rt4:: perl-Test-HTTP-Server-Simple-srpm
rt4:: perl-Text-Password-Pronounceable-srpm
rt4:: perl-Text-Quoted-srpm
rt4:: perl-Text-WikiFormat-srpm
rt4:: perl-Text-Wrapper-srpm
rt4:: perl-Tree-Simple-srpm

#perl-RT-Extension-CommandByMail:: rt4-srpm
#perl-RT-Extension-MandatoryFields:: rt4-srpm

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MFLAGS)) || exit 1

$(RT4PKGS):: rt4repo-7-x86_64.cfg

$(RT4PKGS):: FORCE
	(cd $@ && $(MAKE) $(MFLAGS)) || exit 1

# Needed for local compilation, only use for dev environments
build:: rt4repo.repo

build clean realclean distclean:: FORCE
	@for name in $(EPELPKGS) $(RT4PKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

realclean distclean:: clean

clean::
	find . -name \*~ -exec rm -f {} \;

# Use this only to build completely from scratch
# Leave the rest of rt4repo alone.
maintainer-clean:: clean
	@echo Clearing local yum repository
	find rt4repo -type f ! -type l -exec rm -f {} \; -print

# Leave a safe repodata subdirectory
maintainer-clean:: FORCE

safe-clean:: maintainer-clean FORCE
	@echo Populate rt4repo with empty, safe repodata
	find rt4repo -noleaf -type d -name repodata | while read name; do \
		createrepo -q $$name/..; \
	done

# This is only for upstream repository publication.
# Modify for local use as needed, but do try to keep passwords and SSH
# keys out of the git repository fo this software.
RSYNCTARGET=rsync://localhost/rt4repo
RSYNCOPTS=-a -v --ignore-owner --ignore-group --ignore-existing
RSYNCSAFEOPTS=-a -v --ignore-owner --ignore-group
publish:: all
publish:: FORCE
	@echo Publishing RPMs to $(RSYNCTARGET)
	rsync $(RSYNCSAFEOPTS) --exclude=repodata $(RSYNCTARGET)/

publish:: FORCE
	@echo Publishing repodata to $(RSYNCTARGET)
	find repodata/ -type d -name repodata | while read name; do \
	     rsync $(RSYNCOPTS) $$name/ $(RSYNCTARGET)/$$name/; \
	done

FORCE::
