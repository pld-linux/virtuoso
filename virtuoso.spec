# TODO: -devel/-static split(?), kill unneeded *.la/*.a
Summary:	OpenLink Virtuoso Database System
Summary(pl.UTF-8):	System baz danych OpenLink Virtuoso
Name:		virtuoso
Version:	6.0.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/virtuoso/%{name}-opensource-%{version}.tar.gz
# Source0-md5:	39b68d6c958ad36622ba4476e1ea5fd0
URL:		http://virtuoso.openlinksw.com/
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	net-tools
BuildRequires:	openssl-devel
BuildRequires:	wbxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtuoso is a scalable cross-platform server that combines SQL/RDF/XML
Data Management with Web Application Server and Web Services Platform
functionality.

Virtuoso is at the core a high performance object-relational SQL
database. As a database, it provides transactions, a smart SQL
compiler, powerful stored procedure language with optional Java and
.Net server side hosting, hot backup, SQL 99 and more. It has all
major data access interfaces, as in ODBC, JDBC, ADO .Net and OLE/DB.

Virtuoso has a built-in web server which can serve dynamic web pages
written in Virtuoso's web page language as well as PHP, ASP .Net and
others. This same web server provides SOAP and REST access to Virtuoso
stored procedures, supporting a broad set of WS protocols such as
WS-Security, WS-Reliable Messaging and others. A BPEL4WS run time is
also available as part of Virtuoso's SOA suite.

%description -l pl.UTF-8
Virtuoso to skalowalny, wieloplatformowy serwer łączący funkcjonalność
zarządzania danymi SQL/RDF/XML z serwerem aplikacji WWW i platformą
usług WWW.

Virtuoso opiera się na wysoko wydajnej obiektowo-relacyjnej bazie
danych SQL. Jako baza danych udostępnia transakcje, inteligentny
kompilator SQL, potężny język procedur składowanych z opcjonalną
obsługą Javy i .Net po stronie serwera, backup w czasie rzeczywistym,
SQL 99 i inne. Ma wszystkie ważniejsze interfejsy dostępu do danych,
jak ODBC, JDBC, ADO .Net i OLE/DB.

Virtuoso ma wbudowany serwer WWW, potrafiący obsługiwać dynamiczne
strony napisane we własnym języku Virtuoso, a także PHP, ASP .Net i
innych. Serwer ten daje dostęp SOAP i REST do procedur składowanych
Virtuoso, obsługując szeroki zakres protokołów WS, takich jak
WS-Security, WS-Reliable Messaging i inne. Środowisko uruchomieniowe
BPEL4WS jest także dostępne jako część pakietu Virtuoso SOA.

%prep
%setup -q -n %{name}-opensource-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%doc docsrc/html_virt/*.{html,css,ico}
%attr(755,root,root) %{_bindir}/inifile
%attr(755,root,root) %{_bindir}/isql
%attr(755,root,root) %{_bindir}/isqlw
%attr(755,root,root) %{_bindir}/virt_mail
%attr(755,root,root) %{_bindir}/virtuoso-t

%attr(755,root,root) %{_libdir}/virtodbc.so
%attr(755,root,root) %{_libdir}/virtodbc_r.so
%attr(755,root,root) %{_libdir}/virtodbcu.so
%attr(755,root,root) %{_libdir}/virtodbcu_r.so

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/hosting
%attr(755,root,root) %{_libdir}/%{name}/hosting/creolewiki.so
%attr(755,root,root) %{_libdir}/%{name}/hosting/im.so
%attr(755,root,root) %{_libdir}/%{name}/hosting/mediawiki.so
%attr(755,root,root) %{_libdir}/%{name}/hosting/wbxml2.so
%attr(755,root,root) %{_libdir}/%{name}/hosting/wikiv.so

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/vad
%{_datadir}/%{name}/vad/*.vad
%dir /var/lib/%{name}
/var/lib/%{name}/db
/var/lib/%{name}/vsp
