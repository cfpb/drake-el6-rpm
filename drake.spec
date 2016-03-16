############################
# Set global SPEC variables
############################
#%global _version 1.0.1
%global _version 1.0.2


###############
# Set metadata
###############
Name: drake
Version: %{_version}
Release: 1%{?dist}
Summary: Drake is a simple-to-use, extensible, text-based data workflow tool that organizes command execution around data and its dependencies
Group: Development/Tools
License: Eclipse Public License
URL: http://https://github.com/Factual/drake
#Source: drake
Obsoletes: drake <= 1.0.1
Provides: drake = 1.0.2

%description
Drake is a simple-to-use, extensible, text-based data workflow tool that organizes command execution around data and its dependencies

#####################
# Build requirements
#####################
BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: java


########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh
# code base.  -n defines the name of the directory
# to be Python-2.7 instead of the default, drake27-alt
########################################################
#%prep
#wget -O https://raw.githubusercontent.com/Factual/drake/1.0.1/bin/drake
#%setup 


###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################
%build

git clone https://github.com/Factual/drake

pushd drake
#     git checkout tags/1.0.1 -b 1.0.1
     git checkout develop -b 1.0.2
popd

export DRAKE_HOME=drake

set +e
drake/bin/drake
set -e

# Convenience variable pointing to the directory used for
# PATH's

# Configuring for make, prefix sets the install to /usr/local or
# whatever the setting is.  Enable unicode enables unicode support,
# enable shared builds as a shared library instead of a static library.
# Lastly, since the lib is also installed in /usr/local, tell the
# compiler where it is.



###########################################################


###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.
###########################################################
%install


mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib/drake
mkdir -p %{buildroot}/etc/profile.d

cat drake/bin/drake-pkg | sed 's/DRAKE_JAR/$DRAKE_JAR/g' | tee %{buildroot}/usr/bin/drake

cp drake/target/drake.jar %{buildroot}/usr/lib/drake/

echo "export DRAKE_JAR=/usr/lib/drake/drake.jar" | tee %{buildroot}/etc/profile.d/drake.sh
source %{buildroot}/etc/profile.d/drake.sh
chmod 755 %{buildroot}/usr/bin/drake

###########################################################
# CLEAN
# This directive is for cleaning up post packaging, simply
# removes the buildroot directory in this case.
###########################################################
%clean
# Sanity check before removal of old buildroot files
[ -d "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf %{buildroot}


##############################################################
# FILES
# The files directive must list all files that were installed
# so that they can be included in the package.
##############################################################
%files
%defattr(-,root,root,-)
/usr/bin/drake
/usr/lib/drake/drake.jar
/etc/profile.d/drake.sh

%changelog ] ]
