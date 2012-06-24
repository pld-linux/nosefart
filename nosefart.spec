Summary:	Nosefart - NSF files player
Summary(pl):	Nosefart - odtwarzacz plik�w NSF
Name:		nosefart
Version:	1.92e
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/%{nama}/%{name}-%{version}-mls.tar.bz2
# Source0-md5:	08f8f3e1247fb6c0a0d948a85fb77741
Patch0:		%{name}-opt.patch
URL:		http://nosefart.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nosefart is an NSF files player. NSFs are files which contain the
music code and data from NES games. All that you need to accurately
play the music tracks back are accurate 6502 and NES sound register
emulation.

%description -l pl
Nosefart to odtwarzacz plik�w NSF. NSF to pliki zawieraj�ce kod
odtwarzaj�cy muzyk� oraz dane z gier NES. Do ich odtwarzania potrzebna
jest dok�adna emulacja 6502 i rejestr�w d�wi�kowych NES.

%prep
%setup -q -n %{name}-%{version}-mls
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
