Name:		texlive-dviout-util
Version:	66186
Release:	1
Summary:	DVI output utilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dviout-util
License:	distributable
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviout-util.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviout-util.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
