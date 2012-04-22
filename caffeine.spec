Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.4.419
Release:	%mkrel 1
Group:		Graphical desktop/GNOME
License:	LGPL
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}.desktop
Source12:	%{name}-preferences.desktop
Patch1:		%{name}.desktop.patch
Patch2:		%{name}-preferences.desktop.patch
URL:		https://launchpad.net/~caffeine-developers/+archive/ppa/+packages
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	gettext
BuildRequires:	gettext-devel
Requires:	python-xlib
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
inhibit the screensaver by themselves.

%prep
%setup -q
%patch1 -p0
%patch2 -p0

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --install-lib=%{py_platsitedir}
%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%{_bindir}/caffeine
%{py_platsitedir}/*
%{_datadir}/applications/*
%{_datadir}/caffeine/glade/*.glade
%{_datadir}/caffeine/images/*
%{_iconsdir}/hicolor/*
%{_iconsdir}/ubuntu-mono-dark/*
%{_mandir}/*
%{_datadir}/pixmaps/caffeine.png

