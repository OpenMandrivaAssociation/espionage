Summary:        D-Bus inspector
Name:           espionage
Version:        1.0
Release:        1
License:        LGPLv3+
Group:          Graphical desktop/Enlightenment
Url:            http://enlightenment.org/
Source:         http://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(edje) >= 1.19.1
BuildRequires:  python-efl => 1.19.0
Requires:	pkgconfig(efl) >= 1.19.1
Requires:       python-dbus
Requires:       python-efl => 1.19.0
Requires:       python-lxml
BuildArch:      noarch

%description
Espionage is a complete D-Bus inspector

%files
%doc README COPYING AUTHORS

%{_bindir}/espionage
%{python_sitearch}/espionage/__init__.py
%{python_sitearch}/espionage/espionage.py
%{python_sitearch}/espionage-%{version}-py%{py_ver}.egg-info

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

#%build
%{__python} setup.py build


%install
%{__python} setup.py install --root %{buildroot}


