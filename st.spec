Summary:	Simple terminal
Name:		st
Version:	0.8.4
Release:	1
License:	MIT/X
Group:		X11/Applications
Source0:	https://dl.suckless.org/st/%{name}-%{version}.tar.gz
# Source0-md5:	e00b074c0e5d55513745c99f027b7a34
URL:		https://st.suckless.org/
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
st is a simple terminal emulator for X which sucks less.

%prep
%setup -q

%build
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ LEGACY LICENSE README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/st.1*
