Summary:	Nosefart - NSF files player
Summary(pl):	Nosefart - odtwarzacz plików NSF
Name:		nosefart
Version:	2.6
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/nosefart/%{name}-%{version}-mls.tar.bz2
# Source0-md5:	cbf1cb3658e2042e76a4bb0b35c2ca84
Patch0:		%{name}-opt.patch
Patch1:		%{name}-sh.patch
URL:		http://nosefart.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nosefart is an NSF files player. NSFs are files which contain the
music code and data from NES games. All that you need to accurately
play the music tracks back are accurate 6502 and NES sound register
emulation.

%description -l pl
Nosefart to odtwarzacz plików NSF. NSF to pliki zawieraj±ce kod
odtwarzaj±cy muzykê oraz dane z gier NES. Do ich odtwarzania potrzebna
jest dok³adna emulacja 6502 i rejestrów d¼wiêkowych NES.

%package -n xmms-input-nosefart
Summary:	Nosefart player as XMMS plugin
Summary(pl):	Odtwarzacz Nosefart jako wtyczka XMMS-a
Group:		X11/Applications/Sound

%description -n xmms-input-nosefart
Nosefart is an NSF files player. NSFs are files which contain the
music code and data from NES games. All that you need to accurately
play the music tracks back are accurate 6502 and NES sound register
emulation. This package contains NSF player built as XMMS plugin.

%description -n xmms-input-nosefart -l pl
Nosefart to odtwarzacz plików NSF. NSF to pliki zawieraj±ce kod
odtwarzaj±cy muzykê oraz dane z gier NES. Do ich odtwarzania potrzebna
jest dok³adna emulacja 6502 i rejestrów d¼wiêkowych NES. Ten pakiet
zawiera odtwarzacz zbudowany jako wtyczka XMMS-a.

%package -n gnosefart
Summary:	Graphical player for Nintendo NES audio files
Summary(pl):	Graficzny odtwarzacz plików d¼wiêkowych NES z Nintendo
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description -n gnosefart
gnosefart plays .nsf audio files that were ripped from games for the
Nintendo Entertainment System. It's a GTK+ front end for nosefart.

%description -n gnosefart -l pl
gnosefart odtwarza pliki d¼wiêkowe .nsf wyci±gniête z gier dla konsol
Nintendo Entertainment System. Jest to interfejs GTK+ dla programu
nosefart.

%prep
%setup -q -n %{name}-%{version}-mls
%patch0 -p1
%patch1 -p1

rm -rf src/gnosefart-1.4/autom4te.cache

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd src/xmms
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	AM_LDFLAGS="-lm"

cd ../gnosefart-1.4
rm -f mkinstalldirs
cp -f /usr/share/automake/mkinstalldirs .
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}
install src/xmms/.libs/libnosefart.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%{__make} -C src/gnosefart-1.4 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/nosefart

%files -n xmms-input-nosefart
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/libnosefart.so

%files -n gnosefart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnosefart
%{_datadir}/gnosefart
%{_desktopdir}/gnosefart.desktop
%{_pixmapsdir}/gnosefart.png
