%define modname	Spreadsheet-WriteExcel
%define modver 2.39

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%endif

Summary:	Write cross-platform Excel binary file
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Spreadsheet/Spreadsheet-WriteExcel-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-OLE-Storage_Lite
Requires:	perl-Parse-RecDescent

%description
This package contains the Spreadsheet::WriteExcel perl5 module which
can be used to write (not read) Excel95 binary spreadsheets. It supports
multiple workbook, cell formatting, formulas, hyperlinks and more.

Those spreadsheets will be compatible with Excel 5, 95, 97, 2000,
2002. The generated spreadsheets can also be imported in OpenOffice or
Gnumeric.

%prep
%setup -qn %{modname}-%{modver}

# fix perms
chmod 755 examples/*.pl external_charts/*.pl

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
%makeinstall_std

find %{buildroot} -name 'perllocal.pod' -o -name '.packlist' | xargs rm -f

rm -rf %{buildroot}%{perl_vendorlib}/Spreadsheet/WriteExcel/doc
rm -rf %{buildroot}%{perl_vendorlib}/Spreadsheet/WriteExcel/examples

%files
%doc README Changes examples external_charts
%{_bindir}/chartex
%{perl_vendorlib}/Spreadsheet
%{_mandir}/man1/*
%{_mandir}/man3/*


