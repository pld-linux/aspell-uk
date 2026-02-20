Summary:	Ukrainian dictionary for aspell
Summary(pl.UTF-8):	Słownik ukraiński dla aspella
Name:		aspell-uk
Version:	1.4.0
%define	subv	0
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/uk/aspell6-uk-%{version}-%{subv}.tar.bz2
# Source0-md5:	662f15381d11581758866fd7af43b4d7
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ukrainian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik ukraiński (lista słów) dla aspella.

%prep
%setup -q -n aspell6-uk-%{version}-%{subv}

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
