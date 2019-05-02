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
Release: 1%{?dist}
License: GPL

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/firmware-Qlogic-qla2xxx/archive?at=8.03.02&format=tar.gz&prefix=firmware-qlogic-qla2xxx-8.03.02#/qlogic-qla2xxx-firmware-8.03.02.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/firmware-Qlogic-qla2xxx/archive?at=8.03.02&format=tar.gz&prefix=firmware-qlogic-qla2xxx-8.03.02#/qlogic-qla2xxx-firmware-8.03.02.tar.gz) = b15d273318e67e4f83f0f4dabe9c08000281d981


BuildRequires: kernel-devel

%description
%{vendor_name} %{driver_name} device firmware for the Linux Kernel
version %{kernel_version}.

%prep
%autosetup -p1 -n firmware-%{vendor_label}-%{driver_name}-%{version}

%build

%install
# Put firmware in /lib/firmware/%{kernel_version}
mkdir -p %{buildroot}/%{firmware_dir}
pushd %{_builddir}/firmware-%{vendor_label}-%{driver_name}-%{version}
find . -depth -print | cpio -pdmv %{buildroot}/%{firmware_dir}
popd

%files
%{firmware_dir}/*

%changelog
