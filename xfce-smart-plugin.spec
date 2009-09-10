Summary: 	A Smart plugin for the Xfce panel
Name: 		xfce-smart-plugin
Version: 	0.1.2
Release: 	%mkrel 4
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-smartpm-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-smartpm-plugin/xfce4-smart-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	smart-gui
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Smart plugin for the Xfce panel.

%prep
%setup -qn xfce4-smart-plugin

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-smart-plugin

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-smart-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-smart.desktop
%{_iconsdir}/hicolor/*/apps/*.png


