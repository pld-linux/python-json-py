
%define	module	json-py

Summary:	JSON implementation
Summary(pl):	Rozszerzenie json-py do unittest
Name:		python-json-py
Version:	3.4
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/json-py/json-py-3_4.zip
# Source0-md5:	921ebfede886a10ff32d6d4b4e216f8f
URL:		http://json-py.sf.net/
%pyrequires_eq	python
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
json.py is an implementation of a JSON (http://json.org) reader and
writer in Python.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

install *.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
