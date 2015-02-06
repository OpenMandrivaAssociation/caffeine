Summary:	A system applet that allows to temporarily inhibit screensaver and sleep mode
Name:		caffeine
Version:	2.2.386
Release:	3
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://launchpad.net/~caffeine-developers/+archive/ppa/+packages
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}.desktop
Source12:	%{name}-preferences.desktop
Patch1:		%{name}.desktop.patch
Patch2:		%{name}-preferences.desktop.patch
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caffeine
%{py_platsitedir}/*
%{_datadir}/applications/*
%{_datadir}/caffeine/glade/*.glade
%{_datadir}/caffeine/images/*
%{_iconsdir}/hicolor/*
%{_iconsdir}/ubuntu-mono-dark/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/caffeine.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p0
%patch2 -p0

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --install-lib=%{py_platsitedir}

%find_lang %{name}

