#!/usr/bin/env bash

fileprefix=$(date +'%m-%d-%Y')
comment=$fileprefix"-updall"
sudo timeshift --create --comments $comment


flatpak update

yay -Syyu

doom upgrade
