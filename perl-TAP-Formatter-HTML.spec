#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-TAP-Formatter-HTML
Version  : 0.13
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/TAP-Formatter-HTML-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/TAP-Formatter-HTML-0.13.tar.gz
Summary  : 'TAP Test Harness output delegate for html output'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-TAP-Formatter-HTML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Template)
BuildRequires : perl(URI)
BuildRequires : perl(URI::file)
BuildRequires : perl(accessors)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
TAP::Formatter::HTML - TAP Test Harness output delegate for html output
SYNOPSIS
##
## command-line usage (alpha):
##
prove -m -Q -P HTML=outfile:out.html,css_uri:style.css,js_uri:foo.js,force_inline_css:0

%package dev
Summary: dev components for the perl-TAP-Formatter-HTML package.
Group: Development
Provides: perl-TAP-Formatter-HTML-devel = %{version}-%{release}
Requires: perl-TAP-Formatter-HTML = %{version}-%{release}

%description dev
dev components for the perl-TAP-Formatter-HTML package.


%package perl
Summary: perl components for the perl-TAP-Formatter-HTML package.
Group: Default
Requires: perl-TAP-Formatter-HTML = %{version}-%{release}

%description perl
perl components for the perl-TAP-Formatter-HTML package.


%prep
%setup -q -n TAP-Formatter-HTML-0.13
cd %{_builddir}/TAP-Formatter-HTML-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::Prove::Plugin::HTML.3
/usr/share/man/man3/TAP::Formatter::HTML.3
/usr/share/man/man3/TAP::Formatter::HTML::Session.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
