%define upstream_name	 Spreadsheet-WriteExcel
%define upstream_version 2.37

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Write cross-platform Excel binary file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-OLE-Storage_Lite
BuildArch:	noarch
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
%{_mandir}/*/*


%changelog
* Thu Feb 04 2010 Jérôme Quelin <jquelin@mandriva.org> 2.370.0-1mdv2010.1
+ Revision: 500674
- update to 2.37

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 2.360.0-1mdv2010.1
+ Revision: 494936
- update to 2.36

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 2.350.0-1mdv2010.1
+ Revision: 489517
- update to 2.35

* Fri Jan 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.340.0-1mdv2010.1
+ Revision: 487477
- update to 2.34

* Mon Jan 04 2010 Jérôme Quelin <jquelin@mandriva.org> 2.330.0-1mdv2010.1
+ Revision: 486124
- update to 2.33

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.320.0-1mdv2010.1
+ Revision: 484374
- update to 2.32

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.310.0-1mdv2010.1
+ Revision: 477631
- update to 2.31

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.300.0-1mdv2010.1
+ Revision: 472250
- update to 2.30

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 2.290.0-1mdv2010.1
+ Revision: 470459
- update to 2.29

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 2.280.0-1mdv2010.1
+ Revision: 468888
- update to 2.28

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 2.260.0-1mdv2010.1
+ Revision: 466002
- update to 2.26

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.250.0-1mdv2010.0
+ Revision: 404411
- rebuild using %%perl_convert_version

* Tue Sep 09 2008 Frederik Himpe <fhimpe@mandriva.org> 2.25-1mdv2009.0
+ Revision: 283265
- Add perl-OLE-Storage_Lite buildrequires to try to fix testsuite
- update to new version 2.25

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.23-1mdv2009.0
+ Revision: 270746
- update to new version 2.23

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.22-1mdv2009.0
+ Revision: 239163
- update to new version 2.22

* Tue Mar 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.21-1mdv2008.1
+ Revision: 185192
- update to new version 2.21

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.20-1mdv2008.1
+ Revision: 97564
- update to new version 2.20

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2008.0
+ Revision: 46659
- update to new version 2.18


* Mon May 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.17-1mdv2007.0
- New release 2.17

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.16-1mdk
- New release 2.16
- %%mkrel

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.15-1mdk
- New release 2.15
- spec cleanup
- better summary
- fix perms and encoding

* Thu Jul 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.14-1mdk
- 2.14

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.11-1mdk
- 2.11
- initial mandrake import

* Thu Sep 02 2004 Francis J. Lacoste <flacoste@logreport.org> 0.43-1
- New upstream release.
  - Rebuilt on Fedora Core 2.

