%global tl_name vcell
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	Vertical alignment of content inside table cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vcell
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vcell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vcell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers low-level macros to build rows with vertically-
aligned cells (top, middle or bottom) and calculate the height of a row.
These cells can have variable or fixed height and can be paragraph-cells
or inline-cells. Different vertical alignments can be used in the same
row.

