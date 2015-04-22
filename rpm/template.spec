Name:           ros-jade-rtctree
Version:        3.0.1
Release:        0%{?dist}
Summary:        ROS rtctree package

Group:          Development/Libraries
License:        EPL
URL:            http://ros.org/wiki/openrtm_tools
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  omniORB-devel
BuildRequires:  python-omniORB
BuildRequires:  python-setuptools
BuildRequires:  ros-jade-catkin

%description
API for interacting with running RT-Components and managing RTM-based systems
using OpenRTM-aist.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Apr 22 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.1-0
- Autogenerated by Bloom

