Name: rpm-test
Version: 0.0.1
Release: 1%{?dist}
Summary: just test
URL: https://github.com/cyrnotcry/rpm-test.git
Group: Applications/System
License: GPL
Source: {{{ git_dir_pack }}}
BuildArch: noarch

%description

%prep
%setup -q

%build


%install

%clean

%files

%defattr(-,root,root,0644)
/etc/cron.d/rpm-test.cron

%defattr(-,root,root,0755)
/opt/rpm-test
/var/log/rpm-test

%pre

%post

%preun

%postun
rm -fr /opt/rpm-test
rm -fr /var/log/rpm-test
rm -fr /dev/shm/rpm-test.lock

%changelog

