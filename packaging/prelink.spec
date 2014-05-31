#sbs-git:slp/pkgs/p/prelink prelink 0.0.20100106 53be293a9c8dc4944a4194b79f7d627dd1056a04
Name:       prelink
Summary:    An ELF prelinking utility
Version:    0.0.20100106
Release:    1
Group:      System/Base
License:    GPLv2+
Source0:    http://people.redhat.com/jakub/prelink/%{name}-%{version}.tar.gz
Source1:    prelink.conf
Requires:   /bin/find
Requires:   /bin/awk
Requires:   /bin/grep
BuildRequires:  elfutils-libelf-devel-static
BuildRequires:  glibc-static


%description
The prelink package contains a utility which modifies ELF shared libraries
and executables, so that far fewer relocations need to be resolved at runtime
and thus programs come up faster.




%prep
%setup -q


%build
%configure \
	--disable-shared \
	--disable-libtool-lock \
	--disable-dependency-tracking

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_sysconfdir}
cp -af %{SOURCE1} %{buildroot}%{_sysconfdir}

%remove_docs



%files
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/prelink.conf
%{_prefix}/sbin/prelink
%{_prefix}/bin/execstack


