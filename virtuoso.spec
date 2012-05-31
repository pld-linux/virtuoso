# NOTE:
# - building --with vad requires:
#	- usable netstat 
#	- unused port 1111 (used f.e. by virtuoso-t)
#	- many unpackaged files which should be removed or included in subpackages
#
%bcond_without	vad
#
Summary:	OpenLink Virtuoso Database System
Summary(pl.UTF-8):	System baz danych OpenLink Virtuoso
Name:		virtuoso
Version:	6.1.5
Release:	1
License:	GPL v2
Group:		Applications
# http://dl.sourceforge.net/virtuoso/%{name}-opensource-%{version}.tar.gz
Source0:	%{name}-opensource-%{version}.tar.gz
# Source0-md5:	61b53395e14a11dd7e7715b50261b9eb
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
BuildRequires:	readline-devel
BuildRequires:	libwbxml-devel
BuildRequires:	zlib-devel
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

%package tools
Summary:	Virtuoso tools
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Virtuoso tools.

%package plugins-hosting
Summary:	Hosting plugins for virtuoso
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description plugins-hosting
Hosting plugins for virtuoso.

%package vad
Summary:	VAD applications for virtuoso
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description vad
VAD applications for virtuoso.

%package doc
Summary:	Virtuoso documentation
Group:		Documentation

%description doc
Virtuoso documentation.

%prep
%setup -q -n %{name}-opensource-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=%{_libdir}/%{name} \
	%{!?with_vad:--disable-all-vads} \
	--enable-xml \
	--enable-krb \
	--enable-openssl \
	--enable-openldap \
	--enable-imagemagick \
	--enable-wbxml2 \
	--enable-aio \
	--with-readline \
	--without-internal-zlib \
	--with-pthreads \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s . $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/virtuoso-t

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/virtodbc.so
%attr(755,root,root) %{_libdir}/%{name}/virtodbc_r.so
%attr(755,root,root) %{_libdir}/%{name}/virtodbcu.so
%attr(755,root,root) %{_libdir}/%{name}/virtodbcu_r.so

%dir /var/lib/%{name}
/var/lib/%{name}/db
/var/lib/%{name}/vsp

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/inifile
%attr(755,root,root) %{_bindir}/isql
%attr(755,root,root) %{_bindir}/isqlw
%attr(755,root,root) %{_bindir}/virt_mail

%files plugins-hosting
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{name}/hosting
%attr(755,root,root) %{_libdir}/%{name}/%{name}/hosting/im.so
%attr(755,root,root) %{_libdir}/%{name}/%{name}/hosting/wbxml2.so

%if %{with vad}
%attr(755,root,root) %{_libdir}/%{name}/%{name}/hosting/creolewiki.so
%attr(755,root,root) %{_libdir}/%{name}/%{name}/hosting/mediawiki.so
%attr(755,root,root) %{_libdir}/%{name}/%{name}/hosting/wikiv.so

%files vad
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/vad
%{_datadir}/%{name}/vad/*.vad

%files doc
%defattr(644,root,root,755)
%doc docsrc/html_virt/*.{html,css,ico}
%endif
