Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.9.5
Release:	3
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://launchpad.net/~caffeine-developers/+archive/ppa/+packages
Source0:	https://launchpad.net/~caffeine-developers/+archive/ubuntu/ppa/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
#Source11:	%{name}.desktop
#Source12:	%{name}-preferences.desktop
#Patch1:		%{name}.desktop.patch
#Patch2:		%{name}-preferences.desktop.patch
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(pygtk-2.0)
#BuildRequires:	pkgconfig(python)
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig(python2)

Requires:       python-xlib
Requires:       python-notify
Requires:       python-pyxdg
Requires:       python-dbus

Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	pygtk2.0
Requires:	python-notify
Requires:	python-xlib
BuildArch:	noarch

%description
Caffeine is a system applet that allows the user to temporarily
inhibit both the screensaver and the sleep power saving mode, simply
by clicking on it. This could be useful for example when watching
long flash videos or playing certain full screen games that don't
inhibit the screensaver by themselves

%prep
%setup -qn %{name}
%autopatch -p1

%build
%py2_build

%install
%py2_install
# we don't need ubuntu themes
rm -r %{buildroot}%{_datadir}/icons/ubuntu*
rm -r %{buildroot}%{_sysconfdir}

%find_lang %{name}-indicator

%files -f %{name}-indicator.lang
%doc COPYING COPYING.LESSER README
%{_bindir}/*
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/status/%{name}-*.*
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/*.1*
%{_datadir}/caffeine-indicator/glade/GUI.glade
