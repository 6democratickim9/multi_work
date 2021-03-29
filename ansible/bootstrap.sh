#! /usr/bin/env bash
yum install -y epel-release
yum install -y ansible

mkdir -p /home/vagrant/.vim/autoload /home/vagrant/.vim/bundle
touch /home/vagrant/.vimrc
touch /home/vagrant/.bashrc

