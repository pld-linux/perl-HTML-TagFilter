#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TagFilter
Summary:	HTML::TagFilter - an HTML::Parser-based selective tag remover
Summary(pl):	HTML::TagFilter - wybiórcze usuwanie znaczników oparte o HTML::Parser
Name:		perl-HTML-TagFilter
Version:	0.075
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8225d9362c226ee6c95972a21b9dfdc1
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 1.0
%endif
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
Nazwany tak na próbê HTML::TagFilter jest podklas± HTML::Parser o
jednym celu: usuwaniu niechcianych znaczników HTML i atrybutów z
fragmentu tekstu. Mo¿e dzia³aæ w bardziej lub mniej precyzyjny
sposób - mo¿na podaæ dozwolone znaczniki, dozwolone atrybuty dla
ka¿dego znacznika, dozwolone warto¶ci dla ka¿dego atrybutu w dowolnie
szczegó³owy sposób.

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
