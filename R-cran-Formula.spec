%define		fversion	%(echo %{version} |tr r -)
%define		modulename	Formula
%undefine	_debugsource_packages
Summary:	Extended Model Formulas
Name:		R-cran-%{modulename}
Version:	1.2r5
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	fa5128b436b67051b231e0a8281f36a4
URL:		http://socserv.socsci.mcmaster.ca/jfox/
BuildRequires:	R >= 2.8.1
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-tex-thumbpdf
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Infrastructure for extended formulas with multiple parts on
the right-hand side and/or multiple responses on the left-hand side.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
