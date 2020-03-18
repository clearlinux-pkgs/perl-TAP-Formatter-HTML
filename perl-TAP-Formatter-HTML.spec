#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-TAP-Formatter-HTML
Version  : 0.11
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/TAP-Formatter-HTML-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/TAP-Formatter-HTML-0.11.tar.gz
Summary  : 'TAP Test Harness output delegate for html output'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-TAP-Formatter-HTML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Template)
BuildRequires : perl(URI)
BuildRequires : perl(URI::file)
BuildRequires : perl(accessors)

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
%setup -q -n TAP-Formatter-HTML-0.11
cd %{_builddir}/TAP-Formatter-HTML-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/lib/perl5/vendor_perl/5.30.2/App/Prove/Plugin/HTML.pm
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML.pm
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/Session.pm
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/default_page.css
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/default_report.css
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/default_report.js
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/default_report.tt2
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/jquery-1.4.2.min.js
/usr/lib/perl5/vendor_perl/5.30.2/TAP/Formatter/HTML/jquery.tablesorter-2.0.3.min.js
