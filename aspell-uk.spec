Summary:	Ukrainian dictionary for aspell
Summary(pl):	Ukraiñski s³ownik dla aspella
Name:		aspell-uk
Version:	0.50
%define	subv	3
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/uk/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	0b37b59539424a6980814ce5392725a8
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ukrainian dictionary (i.e. word list) for aspell.

%description -l pl
Ukraiñski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
