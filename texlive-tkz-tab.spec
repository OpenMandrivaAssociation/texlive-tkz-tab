# revision 22834
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-tab
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.3c
Name:		texlive-tkz-tab
Version:	1.3c
Release:	6
Summary:	Tables of signs and variations using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-tab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-tab.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/tkz-tab/tkz-tab.sty
%doc %{_texmfdistdir}/doc/latex/tkz-tab/README
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZ-doc-tab-faq.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-adapt.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-bac.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-examples.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-image.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-init.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-install.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-sign.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-slope.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-style.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-tangente.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-tv.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-valeurs.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab-variation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-tab/latex/TKZdoc-tab.ist
%doc %{_texmfdistdir}/doc/latex/tkz-tab/readme-us.txt
%doc %{_texmfdistdir}/doc/latex/tkz-tab/tkz-tab-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3c-2
+ Revision: 756998
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3c-1
+ Revision: 719769
- texlive-tkz-tab
- texlive-tkz-tab
- texlive-tkz-tab

