Summary:	Ukrainian dictionary for aspell
Summary(pl):	S³ownik ukraiñski dla aspella
Name:		aspell-uk
Version:	0.51
%define	subv	0
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/uk/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	767bfca10c64b239b05cb8b68a78f4ad
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ukrainian dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik (lista s³ów) ukraiñski dla aspella.

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
