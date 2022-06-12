#!/usr/bin/env bash


# Modified off of Mat Weber or LinuxCast
config="$HOME/.config/alacritty/alacritty.yml"

declare -a options=(
"doom-one"
"flat-remix"
"gotham"
"horizondark"
"palenight"
"xterm"
"quit"
)

choice=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -l 20 -p 'Themes')

case $choice in
    'doom-one')
        sed -i '/colors:/c\colors: *doom-one' $config ;;
    'gotham')
        sed -i '/colors:/c\colors: *gotham' $config ;;
    'horizondark')
        sed -i '/colors:/c\colors: *horizondark' $config ;;
    'flat-remix')
        sed -i '/colors:/c\colors: *flat-remix' $config ;;
    'palenight')
        sed -i '/colors:/c\colors: *palenight' $config ;;
    'xterm')
        sed -i '/colors:/c\colors: *xterm' $config ;;

    'quit')
        echo "No theme chosen" && exit 1 ;;
esac
