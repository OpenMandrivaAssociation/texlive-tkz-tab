Name:		texlive-tkz-tab
Version:	66119
Release:	2
Summary:	Tables of signs and variations using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-tab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides comprehensive facilities for preparing
lists of signs and variations, using PGF. The package
documentation requires the tkz-doc bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-tab
%doc %{_texmfdistdir}/doc/latex/tkz-tab

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
