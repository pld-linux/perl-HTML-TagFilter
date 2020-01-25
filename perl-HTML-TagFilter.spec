#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	TagFilter
Summary:	HTML::TagFilter - an HTML::Parser-based selective tag remover
Summary(pl.UTF-8):	HTML::TagFilter - wybiórcze usuwanie znaczników oparte o HTML::Parser
Name:		perl-HTML-TagFilter
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e61d2f180e3ba55e5d71293d472ffebb
URL:		http://search.cpan.org/dist/HTML-TagFilter/
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 1.0
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tentatively titled HTML::TagFilter is a subclass of HTML::Parser
with a single purpose: it will remove unwanted HTML tags and
attributes from a piece of text. It can act in a more or less
fine-grained way - you can specify permitted tags, permitted
attributes of each tag, and permitted values for each attribute in as
much detail as you like.

%description -l pl.UTF-8
Nazwany tak na próbę HTML::TagFilter jest podklasą HTML::Parser o
jednym celu: usuwaniu niechcianych znaczników HTML i atrybutów z
fragmentu tekstu. Może działać w bardziej lub mniej precyzyjny
sposób - można podać dozwolone znaczniki, dozwolone atrybuty dla
każdego znacznika, dozwolone wartości dla każdego atrybutu w dowolnie
szczegółowy sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
