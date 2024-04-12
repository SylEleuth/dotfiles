# <div align="center">My Configuration Files</div>

# <div align="center">[KDE](https://github.com/SylEleuth/gruvbox-plus-kde)</div>
![Screenshot_20240408_141802](https://github.com/SylEleuth/dotfiles/assets/33354262/0f452992-9c46-4e55-bc69-7dc3019d93b5)

<details><summary><b>More info:</b></summary>

- Config files are located in a different <a href="https://github.com/SylEleuth/gruvbox-plus-kde">repo</a>. It's still for 5.27 version but it should be usable in version 6.0 and above, although not tested yet.
- Icon pack is a <a href="https://github.com/SylEleuth/gruvbox-plus-icon-pack">Gruvbox Plus</a>.
- Krunner config is <a href="https://github.com/SylEleuth/dotfiles/tree/master/config/krunner">here</a>. To position it like in the screenshot You have to add custom `Window Rules` in KDE settings (Size & Position).
- Wallpaper by [Hua Lu](https://www.artstation.com/artwork/qAABGD)
</details>

# <div align="center">[Kitty](https://github.com/SylEleuth/dotfiles/tree/master/config/kitty)</div>
![Screenshot_20240408_142014](https://github.com/SylEleuth/dotfiles/assets/33354262/a85c3a05-6c72-4461-8032-e58ce96e431f)

# <div align="center">[Neovim](https://github.com/SylEleuth/dotfiles/tree/master/nvim)</div>
![Screenshot_20240408_165123](https://github.com/SylEleuth/dotfiles/assets/33354262/b333e592-5c1d-4ce2-8bce-37df20a0429e)

# <div align="center">[Vifm](https://github.com/SylEleuth/dotfiles/tree/master/config/vifm)</div>
![Screenshot_20240406_211455](https://github.com/SylEleuth/dotfiles/assets/33354262/bd44a7c2-1e2e-4bd7-b38c-254837473e1e)

<details><summary><b>More info:</b></summary>
<a href="https://github.com/vifm/vifm">Vifm</a> is a file manager with vim key bindings. I use it in a kitty opened in a "scratchpad" with <a href="https://github.com/noctuid/tdrop">tdrop</a>.<br>

`tdrop -maA -w 50% -h 54% -y 46% --monitor DisplayPort-0 kitty --name "dropdown" --config $CONFIG/kitty/kitty-dropdown.conf --session $CONFIG/kitty/startup.conf`

What You see on a screenshot takes a little over than half of the 1920x1080 display.
- `-w` - 50% of display's width
- `-h` - 54% of display's height
- `-y` - opens 46% (approx. 497px) from the top of the display (default 0 for `-x`)
- I'm using two monitors so I had to specify which display to use
- config is a little different comparing to main kitty config (very small details)
</details>
