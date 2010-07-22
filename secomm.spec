Name:		secomm
Version:	0.1
Release:	2%{?dist}
Summary:	Show selinux types that have a given permission

Group:		Admin
License:	GPLv2
URL:		http://github.com/jumanjiman/secomm
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	coreutils

%description
Show the intersection of SELinux target types on which
the given subject types share a common permission.

For example: what target type might I choose for my file or
directory if I need the file to be accessible for PERMISSION from
the following daemons: DAEMON1, DAEMON2, and DAEMON3



%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.asciidoc
%doc COPYING
/usr/bin/secomm



%changelog
* Thu Jul 22 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-2
- new package built with tito


