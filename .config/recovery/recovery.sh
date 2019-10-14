#!/bin/sh
sudo pacman -Syyu yay

for pacmanNames in $(cat ~/.config/recovery/native.txt)

do
	sudo pacman -S --needed $pacmanNames 
done

for yayNames in $(cat ~/.config/recovery/aur.txt)

do
    yay -S --needed $yayNames
done
