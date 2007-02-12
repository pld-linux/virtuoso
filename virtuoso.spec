# TODO: -devel/-static split(?), kill unneeded *.la/*.a
Summary:	OpenLink Virtuoso Database System
Summary(pl.UTF-8):	System baz danych OpenLink Virtuoso
Name:		virtuoso
Version:	4.5.3
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dl.sourceforge.net/virtuoso/%{name}-opensource-%{version}.tar.gz
# Source0-md5:	48f0cf9cd9881b2600a3510fe08d4467
Patch0:		%{name}-destdir.patch
URL:		http://virtuoso.openlinksw.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	openssl-devel
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/im.a
%{_libdir}/im.la
%attr(755,root,root) %{_libdir}/im.so
%{_libdir}/jdbc-2.0/virtjdbc2.jar
%{_libdir}/jdbc-2.0/virtjdbc2ssl.jar
%{_libdir}/jdbc-3.0/virtjdbc3.jar
%{_libdir}/jdbc-3.0/virtjdbc3ssl.jar
%{_libdir}/libvirtuoso-t.a
%{_libdir}/libvirtuoso-t.la
%{_libdir}/virtodbc32.a
%{_libdir}/virtodbc32.la
%attr(755,root,root) %{_libdir}/virtodbc32.so
%{_libdir}/virtodbc32_r.a
%{_libdir}/virtodbc32_r.la
%attr(755,root,root) %{_libdir}/virtodbc32_r.so
%{_libdir}/virtodbc32u.a
%{_libdir}/virtodbc32u.la
%attr(755,root,root) %{_libdir}/virtodbc32u.so
%{_libdir}/virtodbc32u_r.a
%{_libdir}/virtodbc32u_r.la
%attr(755,root,root) %{_libdir}/virtodbc32u_r.so
%dir %{_libdir}/virtuoso-opensource
%{_libdir}/virtuoso-opensource/hosting_sample.a
%{_libdir}/virtuoso-opensource/hosting_sample.la
%attr(755,root,root) %{_libdir}/virtuoso-opensource/hosting_sample.so
%{_libdir}/virtuoso-opensource/plugin_sample.a
%{_libdir}/virtuoso-opensource/plugin_sample.la
%attr(755,root,root) %{_libdir}/virtuoso-opensource/plugin_sample.so
%{_libdir}/wikiv.a
%{_libdir}/wikiv.la
%attr(755,root,root) %{_libdir}/wikiv.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/doc
%dir %{_datadir}/%{name}/doc/html
%{_datadir}/%{name}/doc/html/*.html
%dir %{_datadir}/%{name}/vad
%{_datadir}/%{name}/vad/*.vad
%dir /var/lib/%{name}
/var/lib/%{name}/db
/var/lib/%{name}/demo
/var/lib/%{name}/vsp
