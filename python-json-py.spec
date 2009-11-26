
%define	module	json-py

Summary:	JSON implementation
Summary(pl.UTF-8):	Rozszerzenie json-py do unittest
Name:		python-json-py
Version:	3.4
Release:	5
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/json-py/json-py-3_4.zip
# Source0-md5:	921ebfede886a10ff32d6d4b4e216f8f
URL:		http://json-py.sourceforge.net/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
json.py is an implementation of a JSON (http://json.org/) reader and
writer in Python.

%description -l pl.UTF-8
json.py to implementacja odczytu i zapisu JSON (http://json.org/) w
Pythonie.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/json_py-%{version}-py%{py_ver}.egg-info

install *.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

echo 'Metadata-Version: 1.0
Name: %{module}
Version: %{version}
Summary: %{summary}
Home-page: %{url}
License: %{license}' > $RPM_BUILD_ROOT%{py_sitescriptdir}/json_py-%{version}-py%{py_ver}.egg-info/PKG-INFO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/json_py*
