Summary:	FVWM Themes, configuration framework for FVWM
Summary(pl):	FVWM Themes - szkielet konfiguracji dla FVWM
Name:		fvwm-themes-base
Version:	0.6.0
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://telia.dl.sourceforge.net/sourceforge/fvwm-themes/%{name}-%{version}.tar.gz
Source1:	%{name}-rpm-wa.tar.gz
Source2:	%{name}-install-menu-system.sh
URL:		http://fvwm-themes.sourceforge.org/
Autoreq:	1
Requires:	perl >= 5.004
Requires:	m4
BuildRequires:	XFree86-tools
BuildRequires:	awk
BuildRequires:	fvwm2
BuildRequires:	gnome-core
BuildRequires:	perl
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
FVWM Themes is a powerful configuration framework for FVWM, designed
to be easily extensible and configurable, includes several pre-built
themes, a pack of images and sounds.

This base package contains the theme engine and utilities as well as 8
themes.

%description -l fr
FVWM Themes est un systХme de configuration puissant pour FVWM. Il est
extansible, facilement configurable et contient des thХmes, des images
et des fichiers sons.

Le paquet main contient le moteur et des utilitaires ainsi que 8
thХmes.

%description -l pl
FVWM Themes to potЙ©ny szkielet konfiguracji dla FVWM, stworzony tak,
by byФ Ёatwo rozszerzalnym i konfigurowalnym. Zawiera kilka
predefiniowanych motywСw, zestaw obrazkСw i d╪wiЙkСw.

Ten podstawowy pakiet zawiera silnik motywСw i narzЙdzia oraz 8
motywСw.

%description -l ru
FVWM Themes является мощным окружением для оконного менеджера FVWM.
спроектированным с учетом легкости расширения и конфигурации. Пакет
включает в себя готовые темы, графические и звуковые файлы.

Данный базовый пакет содержит конфигурационные утилиты для
всевозможных манипуляций с темами и 8 тем.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	--disable-run-updatemenu \
	--disable-build-menus \
	--disable-menu-system \
	--with-fvwm-bindir=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} ROOT_PREFIX=$RPM_BUILD_ROOT install

# menu-methode stuff
install -d $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system/
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fvwm/menu-system/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%doc doc/FAQ doc/README.1st doc/colorsets doc/creating-themes
%doc doc/fvwm-themes.lsm
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/*/*

%post
[ -x %{_bindir}/fvwm-themes-menuapp ] && %{_bindir}/fvwm-themes-menuapp --site --build-menus --remove-popup || true
sh %{_datadir}/fvwm/menu-system/install-menu-system.sh Install
echo ""
echo "    If you are running fvwm-themes now, to avoid problems choose"
echo "    'Reset all to the default' from the Theme Management menu."
echo ""

%preun
[ -f %{_datadir}/fvwm/menu-system/install-menu-system.sh ] && sh %{_datadir}/fvwm/menu-system/install-menu-system.sh Uninstall || true

## TODO: how to specify the current date in .spec? Or how to run a `command`?
#%changelog
#
#* Tue 23 Oct 2001 18:52:00 UTC  olicha  <olivier.chapuis@free.fr>
#- added a way to handle the debian menu system on any system
#
#* Thu 07 Sep 2000 20:00:00 IDT  FVWM Themes Developers  <fvwm-themes-devel@lists.sourceforge.net>
#- Auto building %{PACKAGE_VERSION}
#
#* Thu 07 Sep 2000 20:00:00 IDT  Mikhael Goikhman  <migo@homemail.com>
#- First try at making the package
