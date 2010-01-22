%define upstream_name	 Spreadsheet-WriteExcel
%define upstream_version 2.36

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Write cross-platform Excel binary file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-OLE-Storage_Lite
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-Parse-RecDescent

%description
This package contains the Spreadsheet::WriteExcel perl5 module which
can be used to write (not read) Excel95 binary spreadsheets. It supports
multiple workbook, cell formatting, formulas, hyperlinks and more.

Those spreadsheets will be compatible with Excel 5, 95, 97, 2000,
2002. The generated spreadsheets can also be imported in OpenOffice or
Gnumeric.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# fix perms
chmod 755 examples/*.pl external_charts/*.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

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
%doc README Changes examples external_charts
%{_bindir}/chartex
%{perl_vendorlib}/Spreadsheet
%{_mandir}/*/*
