#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	OpenLink Virtuoso Database System
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

%prep
%setup -q -n %{name}-opensource-%{version}
%patch0 -p1

%build
#%%{__intltoolize}
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/im.a
%{_prefix}/lib/im.la
%{_prefix}/lib/im.so
%{_prefix}/lib/jdbc-2.0/virtjdbc2.jar
%{_prefix}/lib/jdbc-2.0/virtjdbc2ssl.jar
%{_prefix}/lib/jdbc-3.0/virtjdbc3.jar
%{_prefix}/lib/jdbc-3.0/virtjdbc3ssl.jar
%{_prefix}/lib/libvirtuoso-t.a
%{_prefix}/lib/libvirtuoso-t.la
%{_prefix}/lib/virtodbc32.a
%{_prefix}/lib/virtodbc32.la
%{_prefix}/lib/virtodbc32.so
%{_prefix}/lib/virtodbc32_r.a
%{_prefix}/lib/virtodbc32_r.la
%{_prefix}/lib/virtodbc32_r.so
%{_prefix}/lib/virtodbc32u.a
%{_prefix}/lib/virtodbc32u.la
%{_prefix}/lib/virtodbc32u.so
%{_prefix}/lib/virtodbc32u_r.a
%{_prefix}/lib/virtodbc32u_r.la
%{_prefix}/lib/virtodbc32u_r.so
%{_prefix}/lib/virtuoso-opensource/hosting_sample.a
%{_prefix}/lib/virtuoso-opensource/hosting_sample.la
%{_prefix}/lib/virtuoso-opensource/hosting_sample.so
%{_prefix}/lib/virtuoso-opensource/plugin_sample.a
%{_prefix}/lib/virtuoso-opensource/plugin_sample.la
%{_prefix}/lib/virtuoso-opensource/plugin_sample.so
%{_prefix}/lib/wikiv.a
%{_prefix}/lib/wikiv.la
%{_prefix}/lib/wikiv.so
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
