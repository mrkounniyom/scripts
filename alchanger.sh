#!/usr/bin/env bash


# Modified off of Mat Weber or LinuxCast
config="$HOME/.config/alacritty/alacritty.yml"

declare -a options=(
"doom-one"
"gotham"
"horizondark"
"flat-remix"
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

    'quit')
        echo "No theme chosen" && exit 1 ;;
esac
