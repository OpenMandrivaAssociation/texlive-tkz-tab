%global tl_name tkz-tab
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.12c
Release:	%{tl_revision}.1
Summary:	Tables of signs and variations using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-tab
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides comprehensive facilities for preparing lists of
signs and variations, using PGF. The package documentation requires the
tkz-doc bundle. This package has been taken temporarily out of
circulation to give the author time to investigate some problems.

