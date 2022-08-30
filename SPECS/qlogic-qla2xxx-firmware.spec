%global package_speccommit 195079a2f9451b5406d6d5abdac0a843568e550c
%global usver 8.03.02
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit 8.03.02
%define vendor_name Qlogic
%define vendor_label qlogic
%define driver_name qla2xxx

%if %undefined module_dir
%define module_dir updates
%define firmware_dir /lib/firmware/updates/%{kernel_version}
%else
%define firmware_dir /lib/firmware/%{kernel_version}
%endif

Summary: %{vendor_name} %{driver_name} firmware
Name: %{vendor_label}-%{driver_name}-firmware
Version: 8.03.02
Release: %{?xsrel}%{?dist}
License: GPL
Source0: qlogic-qla2xxx-firmware-8.03.02.tar.gz

BuildRequires: kernel-devel

%description
%{vendor_name} %{driver_name} device firmware for the Linux Kernel
version %{kernel_version}.

%prep
%autosetup -p1 -n %{vendor_label}-%{driver_name}-firmware-%{version}

%build

%install
mkdir -p %{buildroot}/%{firmware_dir}
pushd %{_builddir}/%{vendor_label}-%{driver_name}-firmware-%{version}
find . -depth -print | cpio -pdmv %{buildroot}/%{firmware_dir}
popd

%files
%{firmware_dir}/*

%changelog
* Tue Dec 01 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 8.03.02-2
- CP-35517: Convert to Koji
