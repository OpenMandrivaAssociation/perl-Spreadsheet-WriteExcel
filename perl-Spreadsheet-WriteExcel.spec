%define module	Spreadsheet-WriteExcel
%define name	perl-%{module}
%define version	2.25
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Write cross-platform Excel binary file
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Spreadsheet/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	perl-Parse-RecDescent
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains the Spreadsheet::WriteExcel perl5 module which
can be used to write (not read) Excel95 binary spreadsheets. It supports
multiple workbook, cell formatting, formulas, hyperlinks and more.

Those spreadsheets will be compatible with Excel 5, 95, 97, 2000,
2002. The generated spreadsheets can also be imported in OpenOffice or
Gnumeric.

%prep
%setup -q -n %{module}-%{version}

# fix perms
chmod 755 examples/*.pl charts/*.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name 'perllocal.pod' -o -name '.packlist' | xargs rm -f

rm -rf %{buildroot}/%{perl_vendorlib}/Spreadsheet/WriteExcel/doc
rm -rf %{buildroot}/%{perl_vendorlib}/Spreadsheet/WriteExcel/examples

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes doc examples charts
%{_bindir}/chartex
%{perl_vendorlib}/Spreadsheet
%{_mandir}/*/*

