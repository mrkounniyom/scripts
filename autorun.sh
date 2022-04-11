#!/usr/bin/env bash

picom &
emacs --daemon &
thunar --daemon &
nitrogen --random ~/wallpapers/ --set-scaled
#qxkb &
