Name:		texlive-vcell
Version:	59039
Release:	2
Summary:	Vertical alignment of content inside table cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vcell
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vcell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vcell.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers low-level macros to build rows with
vertically-aligned cells (top, middle or bottom) and calculate
the height of a row. These cells can have variable or fixed
height and can be paragraph-cells or inline-cells. Different
vertical alignments can be used in the same row.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/vcell
%doc %{_texmfdistdir}/doc/latex/vcell

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
