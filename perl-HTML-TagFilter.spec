#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TagFilter
Summary:	HTML::TagFilter - an HTML::Parser-based selective tag remover
Summary(pl):	HTML::TagFilter - wybiórcze usuwanie znaczników w oparciu o HTML::Parser
Name:		perl-HTML-TagFilter
Version:	0.07
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{!?_without_tests:1}0
BuildRequires:	perl-HTML-Parser >= 1.0
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
