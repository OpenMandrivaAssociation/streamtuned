%define name	streamtuned
%define version	0.16.2
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Audio/Video stream player and recorder
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-v0.16_2.tar.bz2
Source1:	shoutcast.pl.bz2
URL:		http://home.kabelfoon.nl/~moongies/streamtuned.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick qt3-devel
BuildRequires:	fftw2-devel
Requires:	wget perl-XML-Simple perl-XML-DOM mplayer

%description
StreamTuned plays and records audio and video streams using mplayer as
backend. It also reads stream url's and related information from playlists,
webpages or XML/RSS feeds. Streamtuned can act as Podcast client and allows
for local and remote (weservice) access to the repositories containing your
stream url's. 

%prep
%setup -q -n %name-0.16

%build
qmake %name.pro
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall INSTALL_ROOT=%buildroot
bzcat %{SOURCE1} > %buildroot/%_datadir/%name/parsers/shoutcast.pl
chmod 755 %buildroot/%_datadir/%name/parsers/*.pl

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=StreamTuned
Comment=A/V stream recorder
Categories=Audio;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 misc/stream_icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 misc/stream_icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 misc/stream_icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc bugs README misc
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

