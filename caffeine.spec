Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.9.12
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://launchpad.net/caffeine
#Source0:	https://launchpad.net/~caffeine-developers/+archive/ubuntu/ppa/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
Source0:  https://files.pythonhosted.org/packages/source/c/cups-of-caffeine/cups-of-caffeine-%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(python)
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
%autosetup -n cups-of-caffeine-%{version} -p1

%build
%py_build

%install
%py_install
# we don't need ubuntu themes
rm -r %{buildroot}%{_datadir}/icons/ubuntu*
rm -r %{buildroot}%{_sysconfdir}

%find_lang %{name}-indicator

%files -f %{name}-indicator.lang
#doc COPYING COPYING.LESSER README
%{_bindir}/caffeinate
%{_bindir}/caffeine
%{_bindir}/caffeine-indicator
%{_datadir}/applications/caffeine-indicator.desktop
%{_datadir}/applications/caffeine.desktop
%{_datadir}/caffeine-indicator/glade/GUI.glade
%{_iconsdir}/hicolor/16x16/apps/*
%{_iconsdir}/hicolor/*x*/status/*
%{_iconsdir}/hicolor/scalable/apps/caffeine.svg
%{_iconsdir}/hicolor/scalable/status/caffeine-cup-empty.svg
%{_iconsdir}/hicolor/scalable/status/caffeine-cup-full.svg
%{python_sitelib}/cups_of_caffeine-%{version}-py*.*.egg-info

