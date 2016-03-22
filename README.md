RPM Spec file for the drake tool

**Description**: Drake is a simple-to-use, extensible, text-based data workflow tool that organizes command execution around data and its dependencies.  https://github.com/Factual/drake 

## Dependencies

Currently, only RHEL and CentOS 6.5 have been tested.  Other dependencies are installed
via the boostrap.sh script.

## Installation

### Build the RPM using Vagrant

1. Once the repo has been cloned, run "vagrant up" to create the bulid VM
2. Run "vagrant ssh" to connect
3. CD to ~/rpmbuild
4. Run "rpmbuild -ba SPECS/drake.spec"

### Build the RPM on a server
1. Once the repo has been cloned, run "sh ./bootstrap.sh"
2. CD to ~/rpmbuild
3. Run "rpmbuild -ba SPECS/drake.spec"

### Install the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/drake.rpm"

## Configuration

Edit the SPEC file to make changes to the build configuration.

## Usage

Drake will be installed in /usr/bin

