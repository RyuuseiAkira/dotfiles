#!/usr/bin/env sh
HYPRGAMEMODE=$(hyprctl getoption animations:enabled | sed -n '1p' | awk '{print $2}')

# Waybar performance
#FILE="$HOME/.config/waybar/style.css"

#sed -i 's/\/\* \(.*animation:.*\) \*\//\1/g' $FILE
#sed -i 's/\/\* \(.*transition:.*\) \*\//\1/g' $FILE
#if [ $HYPRGAMEMODE = 1 ]; then
#	sed -i 's/^\(.*animation:.*\)$/\/\* \1 \*\//g' $FILE
#	sed -i 's/^\(.*transition:.*\)$/\/\* \1 \*\//g' $FILE
#fi
#killall waybar
#waybar >/dev/null 2>&1 &

# Hyprland performance
if [ $HYPRGAMEMODE = 1 ]; then
	hyprctl --batch "\
        keyword animations:enabled 0;\
        keyword decoration:shadow:enabled 0;\
        keyword decoration:active_opacity 1;\
        keyword decoration:inactive_opacity 1;\
        keyword decoration:blur:enabled 0;\
        keyword general:gaps_in 0;\
        keyword general:gaps_out 0;\
        keyword general:border_size 1;\
        keyword decoration:rounding 0"
        killall swww-daemon
	exit
else
	cd /home/akira/.local/share/bin && ./swwwallpaper.sh
        hyprctl reload
fi
