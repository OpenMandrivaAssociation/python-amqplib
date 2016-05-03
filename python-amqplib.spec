%define module  amqplib

Summary:    Python AMQP (Advanced Message Queuing Protocol) client library
Name:       python-%{module}
Version:    1.0.2
Release:    4
Source0:    https://pypi.python.org/packages/source/a/amqplib/amqplib-%{version}.tgz
License:    LGPLv2.1
Group:      Development/Python
Url:        http://code.google.com/p/py-amqplib/
BuildArch:  noarch
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python3-devel
%rename	python3-%{module}

%description
amqplib is a Python client library that supports the 0-8 AMQP
(Advanced Message-Queuing Protocol) spec.

%package -n python2-amqplib
Summary:        Python AMQP (Advanced Message Queuing Protocol) client library
Group:          Development/Python
BuildRequires:  python2-devel
Requires:       python
 
%description -n python2-amqplib
amqplib is a Python client library that supports the 0-8 AMQP
(Advanced Message-Queuing Protocol) spec.

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot} 
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-amqplib
%doc python3/README 
%{python_sitelib}/amqplib/*
%{python_sitelib}/*.egg-info

%files -n python2-amqplib
%doc python2/README
%{python2_sitelib}/amqplib/*
%{python2_sitelib}/*.egg-info
