#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Dist
%define		pnam	CheckConflicts
%include	/usr/lib/rpm/macros.perl
Summary:	Dist::CheckConflicts - declare version conflicts for your dist
Summary(pl.UTF-8):	Dist::CheckConflicts - deklarowanie wersji będących w konflikcie z pakietem
Name:		perl-Dist-CheckConflicts
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Dist/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64b8d342ba11336b2969c274a60bbc5f
URL:		http://search.cpan.org/dist/Dist-CheckConflicts/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils >= 0.12
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One shortcoming of the CPAN clients that currently exist is that they
have no way of specifying conflicting downstream dependencies of
modules. This module attempts to work around this issue by allowing
you to specify conflicting versions of modules separately, and deal
with them after the module is done installing.

For instance, say you have a module Foo, and some other module Bar
uses Foo. If Foo were to change its API in a non-backwards-compatible
way, this would cause Bar to break until it is updated to use the new
API. Foo can't just depend on the fixed version of Bar, because this
will cause a circular dependency (because Bar is already depending on
Foo), and this doesn't express intent properly anyway - Foo doesn't
use Bar at all. The ideal solution would be for there to be a way to
specify conflicting versions of modules in a way that would let CPAN
clients update conflicting modules automatically after an existing
module is upgraded, but until that happens, this module will allow
users to do this manually.

%description -l pl.UTF-8
Jednym z obecnych niedociągnięć klientów CPAN jest to, że nie ma
sposobu określenia zależności będących w konflikcie z modułami.
Niniejszy moduł próbuje obejść ten problem pozwalając określić
osobno wersje modułów będących w konflikcie i obsłużenie ich po
zainstalowaniu modułu.

Na przykład: mamy moduł Foo, a inny moduł Bar używa Foo. Jeśli Foo
zmieni swoje API bez kompatybilności wstecznej, spowoduje to zepsucie
Bar do jego uaktualnienia pod kątem nowego API. Foo nie może
zwyczajnie zależeć od poprawionej wersji Bar, bo spowodowałoby to
zależność cykliczną (ponieważ Bar już zależy od Foo) i nie wyraża
właściwie intencji - Foo w ogóle nie używa Bar. Idealnym rozwiązaniem
byłoby zapewnienie sposobu określania wersji modułów będących w
konflikcie w sposób pozwalający klientom CPAN na automatyczne
uaktualnienie będących w konflikcie modułów po uaktualnieniu
istniejącego modułu - ale zanim to nastąpi, ten moduł pozwala
użytkownikom uczynić to ręcznie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Dist/CheckConflicts.pm
%{_mandir}/man3/Dist::CheckConflicts.3pm*
