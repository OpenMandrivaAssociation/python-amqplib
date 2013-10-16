%define	module	amqplib
%define name	python-%{module}
%define version 1.0.0
%define release %mkrel 1

Summary:	Python AMQP (Advanced Message Queuing Protocol) client library
Name:		%{name}
Version:	1.0.2
Release:	1
Source0:	https://pypi.python.org/packages/source/a/amqplib/amqplib-%{version}.tgz
License:	LGPLv2.1
Group:		Development/Python
Url:		http://code.google.com/p/py-amqplib/
BuildArch:	noarch
BuildRequires:	python-devel

%description
amqplib is a Python client library that supports the 0-8 AMQP
(Advanced Message-Queuing Protocol) spec.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean

%files -f FILE_LIST
%doc README


%changelog
* Fri Aug 05 2011 Lev Givon <lev@mandriva.org> 1.0.0-1mdv2012.0
+ Revision: 693343
- Update to 1.0.0.

* Sun Nov 07 2010 Lev Givon <lev@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 594848
- import python-amqplib



