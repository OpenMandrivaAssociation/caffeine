Summary:	Caffeine is a tiny cup of coffee that sits idly in your system tray waiting for you to click it
Name:		caffeine
Version:	2.2.386
Release:	%mkrel 1
Group:		Graphical desktop/GNOME
License:	LGPL
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
URL:		https://launchpad.net/~caffeine-developers/+archive/ppa/+packages
BuildRequires: 	pygtk2.0-devel
BuildRequires: 	libpython-devel 
BuildRequires:	gettext
BuildRequires:  gettext-devel
Requires:       python-xlib 
Requires:	pygtk2.0
Requires:	gnome-python
Requires:	python-notify
Requires:	gnome-python-gconf
BuildArch:	noarch

%description
Caffeine is a system applet that allows the user to temporarily
inhibit both the screensaver and the sleep power saving mode, simply
by clicking on it. This could be useful for example when watching 
long flash videos or playing certain full screen games that don't
inhibit the screensaver by themselves 

%prep
%setup -q -n %{name}-%{version}

%build

python setup.py build

%install

rm -rf %{buildroot}

python setup.py install --root=$RPM_BUILD_ROOT --install-lib=%{py_platsitedir}

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%_bindir/caffeine
%{py_platsitedir}/*
%_datadir/applications/*
%_datadir/caffeine/glade/*.glade
%_datadir/caffeine/images/*
%_iconsdir/hicolor/*
%_iconsdir/ubuntu-mono-dark/*
%{_mandir}/*
%_datadir/pixmaps/caffeine.png
