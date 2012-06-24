Summary:	FVWM Themes, configuration framework for FVWM
Summary(pl):	FVWM Themes - szkielet konfiguracji dla FVWM
Name:		fvwm-themes-base
Version:	0.6.0
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/fvwm-themes/%{name}-%{version}.tar.gz
Source1:	%{name}-rpm-wa.tar.gz
Source2:	%{name}-install-menu-system.sh
Patch0:		%{name}-DESTDIR.patch
URL:		http://fvwm-themes.sourceforge.org/
BuildRequires:	XFree86-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fvwm2
BuildRequires:	gnome-core
BuildRequires:	perl
Requires:	perl >= 5.004
Requires:	m4
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FVWM Themes is a powerful configuration framework for FVWM, designed
to be easily extensible and configurable, includes several pre-built
themes, a pack of images and sounds.

This base package contains the theme engine and utilities as well as 8
themes.

%description -l fr
FVWM Themes est un syst�me de configuration puissant pour FVWM. Il est
extansible, facilement configurable et contient des th�mes, des images
et des fichiers sons.

Le paquet main contient le moteur et des utilitaires ainsi que 8
th�mes.

%description -l pl
FVWM Themes to pot�ny szkielet konfiguracji dla FVWM, stworzony tak,
by by� �atwo rozszerzalnym i konfigurowalnym. Zawiera kilka
predefiniowanych motyw�w, zestaw obrazk�w i d�wi�k�w.

Ten podstawowy pakiet zawiera silnik motyw�w i narz�dzia oraz 8
motyw�w.

%description -l ru
FVWM Themes �������� ������ ���������� ��� �������� ��������� FVWM.
���������������� � ������ �������� ���������� � ������������. �����
�������� � ���� ������� ����, ����������� � �������� �����.

������ ������� ����� �������� ���������������� ������� ���
������������ ����������� � ������ � 8 ���.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-run-updatemenu \
	--disable-build-menus \
	--disable-menu-system \
	--with-fvwm-bindir=%{_bindir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# menu-methode stuff
install -d $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/fvwm-themes-menuapp ] && %{_bindir}/fvwm-themes-menuapp --site --build-menus --remove-popup || true
sh %{_datadir}/fvwm/menu-system/install-menu-system.sh Install
echo ""
echo "    If you are running fvwm-themes now, to avoid problems choose"
echo "    'Reset all to the default' from the Theme Management menu."
echo ""

%preun
[ -f %{_datadir}/fvwm/menu-system/install-menu-system.sh ] && sh %{_datadir}/fvwm/menu-system/install-menu-system.sh Uninstall || true

%files
%defattr(644,root,root,755)
# COPYING is a short note, doesn't contain full GPL text
%doc AUTHORS COPYING INSTALL NEWS README TODO
%doc doc/FAQ doc/README.1st doc/colorsets doc/creating-themes
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/fvwm/images
%dir %{_datadir}/fvwm/locale
%{_datadir}/fvwm/locale/en
%lang(fr) %{_datadir}/fvwm/locale/fr
%lang(ja) %{_datadir}/fvwm/locale/ja
%lang(ru) %{_datadir}/fvwm/locale/ru
%{_datadir}/fvwm/menu-system
%{_datadir}/fvwm/sounds
%{_datadir}/fvwm/themes
%{_datadir}/fvwm/Fvwm*
