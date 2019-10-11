#!/bin/sh
sudo pacman -Syyu yay

for pacmanNames in $(cat ~/.config/recovery/pacman.txt)

do
	sudo pacman -S --needed $pacmanNames 
done

for yayNames in $(cat ~/.config/recovery/yay.txt)

do
    yay -S --needed $yayNames
done
