export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/nvim
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
# fix "xdg-open fork-bomb" export your preferred browser from here
export BROWSER=/usr/bin/firefox

xmodmap -e "clear lock" #disable caps lock switch
xmodmap -e "keysym Caps_Lock = Escape" #set caps_lock as escape

# # This file depends on settings in .Xmodmap
# xmodmap /home/eleuth/.Xmodmap

# # Use Spacebar as a Modifier
# spare_modifier="Hyper_L" 
# xmodmap -e "keycode 65 = $spare_modifier"   
# xmodmap -e "add Hyper_L = $spare_modifier"
# xmodmap -e "keycode any = space"  
# xcape -e "$spare_modifier=space"
