#
# spec file for package supportutils-plugin-groupwise (Version 0.0-0)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-groupwise
URL:          https://code.google.com/p/supportutils-plugin-groupwise/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      0.0
Release:      0
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for Groupwise
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource-0.0.1

%description
Supportconfig plugin for Groupwise. Informaiton is gathered for Groupwise 
Agents, Monitor, GWIA and WebAcces. Supportconfig saves the plugin output 
as plugin-groupwise.txt.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-groupwise/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f groupwise-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0500 groupwise $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 groupwise-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/groupwise-plugin.8.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/*
/usr/share/man/man8/groupwise-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-groupwise
