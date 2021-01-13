Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.9.8
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://launchpad.net/~caffeine-developers/+archive/ppa/+packages
Source0:	https://launchpad.net/~caffeine-developers/+archive/ubuntu/ppa/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	gettext-devel
#BuildRequires:	pkgconfig(python)
BuildRequires:  gobject-introspection

Requires:       python-xlib
Requires:       python-notify
Requires:       python3dist(pyxdg)
Requires:       python-dbus
BuildArch:	noarch

%description
Caffeine is a system applet that allows the user to temporarily
inhibit both the screensaver and the sleep power saving mode, simply
by clicking on it. This could be useful for example when watching
long flash videos or playing certain full screen games that don't
inhibit the screensaver by themselves

%prep
%setup -qn %{name}-%{version}
%autopatch -p1

%build
%py_build

%install
%py_install
# we don't need ubuntu themes
rm -r %{buildroot}%{_datadir}/icons/ubuntu*
rm -r %{buildroot}%{_sysconfdir}

%find_lang %{name}-indicator

%files -f %{name}-indicator.lang
%doc COPYING COPYING.LESSER README
%{_bindir}/*
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/status/%{name}-*.*
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/*.1*
%{_datadir}/caffeine-indicator/glade/GUI.glade
