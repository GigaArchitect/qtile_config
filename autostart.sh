#!/usr/bin/env bash 
mouse_id=$(xinput list | grep "HID 1bcf:08a0 Mouse" | grep -o "id=[0-9]*" | grep -o "[0-9]*")
prop=$(xinput list-props $mouse_id | grep "libinput Accel Speed ([0-9]*):" | grep -o "[0-9]*" | head -n1)
xinput set-prop $mouse_id $prop -1 &
redshift -c ~/.config/redshift/redshift.conf &
copyq &
#lxsession &
dunst &
udiskie &
light -N 5 &
/usr/lib/xfce-polkit/xfce-polkit &
unclutter &
numlockx on &
blueman-applet &
spectacle -s &
#xrandr --output eDP-1 --gamma .85:.85:.82 &
#xrandr --output eDP-1 --gamma .85 &
picom &
nm-applet &
xss-lock --transfer-sleep-lock -- i3lock -B sigma --nofork &
### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
nitrogen --restore &
