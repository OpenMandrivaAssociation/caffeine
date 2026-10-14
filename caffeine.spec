Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.10.1
Release:	1
License:	GPLv3+ and LGPLv3+
Group:		Graphical desktop/GNOME
URL:		https://launchpad.net/caffeine
Source0:	https://files.pythonhosted.org/packages/source/c/cups-of-caffeine/cups_of_caffeine-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	python%{pyver}dist(ewmh)
Requires:	python%{pyver}dist(python-xlib)
Requires:	python%{pyver}dist(pygobject)
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(AyatanaAppIndicator3) = 0.1
Requires:	typelib(Keybinder) = 3.0
Requires:	xdg-utils

%description
Caffeine is a system applet that allows the user to temporarily
inhibit both the screensaver and the sleep power saving mode, simply
by clicking on it. This could be useful for example when watching
long flash videos or playing certain full screen games that don't
inhibit the screensaver by themselves.

%prep
%autosetup -n cups_of_caffeine-%{version} -p1

%build
%py_build

%install
%py_install
# share/ lives at the sdist root, so the wheel does not install it.
# glade is not listed in package-data, and the applet loads it from
# the installed package directory.
/bin/cp -a share/. %{buildroot}%{_datadir}/
rm -rf %{buildroot}%{_datadir}/icons/ubuntu-mono-dark
rm -rf %{buildroot}%{_datadir}/icons/ubuntu-mono-light
/bin/cp -a cups_of_caffeine/glade %{buildroot}%{python_sitelib}/cups_of_caffeine/

%files
%license COPYING COPYING.LESSER
%doc README.md
%{_bindir}/caffeine
%{_bindir}/caffeine-indicator
%{_bindir}/caffeinate
%{_datadir}/applications/caffeine.desktop
%{_datadir}/applications/caffeine-indicator.desktop
%{_datadir}/caffeine-indicator/
%{_datadir}/glib-2.0/schemas/org.sc3d.caffeine.gschema.xml
%{_datadir}/pixmaps/caffeine.png
%{_mandir}/man1/caffeine.1*
%{_mandir}/man1/caffeine-indicator.1*
%{_mandir}/man1/caffeinate.1*
%{_iconsdir}/hicolor/
%{python_sitelib}/cups_of_caffeine
%{python_sitelib}/cups*caffeine-%{version}*
