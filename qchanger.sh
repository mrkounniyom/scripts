#!/usr/bin/env bash

# Modified off of Mat Weber or LinuxCast
config="$HOME/.config/qtile/config.py"

declare -a options=(
"1337"
"Challenger Deep"
"Doom-One"
"Nord"
"Unknown"
"quit"
)

choice=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -l 20 -p 'Themes')

case $choice in
    'Challenger Deep')
        sed -i '/colors =/c\colors = qtheme.challenger_deep' $config && qtile cmd-obj -o cmd -f restart ;;
    '1337')
        sed -i '/colors =/c\colors = qtheme.i337' $config && qtile cmd-obj -o cmd -f restart ;;
    'Nord')
        sed -i '/colors =/c\colors = qtheme.nord' $config && qtile cmd-obj -o cmd -f restart ;;
    'Unknown')
        sed -i '/colors =/c\colors = qtheme.notSure' $config && qtile cmd-obj -o cmd -f restart ;;
    'Doom-One')
        sed -i '/colors =/c\colors = qtheme.doom_one' $config && qtile cmd-obj -o cmd -f restart ;;


    'quit')
        echo "No theme chosen" && exit 1 ;;
esac
