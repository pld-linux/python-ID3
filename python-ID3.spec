
%define		module	ID3

Summary:	Module for manipulating ID3 informational tags on MP3 audio files
Summary(pl.UTF-8):	Moduł służący do manipulacji znacznikami ID3 plików MP3
Name:		python-%{module}
Version:	1.2
Release:	5
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/id3-py/id3-py_%{version}.tar.gz
# Source0-md5:	de0bd6053dda674967dacb6492a90c69
URL:		http://id3-py.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple Python module for retrieving and setting so-called
ID3 tags on MP3 compressed audio files through an object-oriented
interface. MP3 players generally use this simple information for
display track title, artist name, and album title while playing the
sound file.

ID3.py supports ID3 version 1.1, including the track number field. I
have no current plans to code up the monstrosity that is ID3v2
(http://www.id3.org/id3v2.3.0.html) but if someone wants to add that
functionality, feel free!

%description -l pl.UTF-8
Jest to prosty moduł Pythona służący do pobierania i ustawiania tak
zwanych znaczników ID3 ze skompresowanych plików audio MP3 poprzez
obiektowy interfejs. Odtwarzacze MP3 korzystają z tych prostych
informacji do wyświetlania numeru ścieżki, nazwy twórcy i tytułu
albumu w czasie odtwarzania pliku.

ID3.py obsługuje taki ID3 w wersji 1.1, włączając w to numery ścieżek.
Chwilowo nie jest planowana obsługa ID3v2
(http://www.id3.org/id3v2.3.0.html) - chętni do dodania takiej obsługi
proszeni są o kontakt z autorem.

%prep
%setup -q -n id3-py-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install id3-tagger.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitescriptdir}/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
