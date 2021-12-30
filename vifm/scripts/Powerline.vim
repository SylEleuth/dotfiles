" STATUS LINE "
"""""""""""""""

" SEPARATORS "
let L_B=""
let L_T=""
let R_B=""
let R_T=""

" COLORS "
""""""""""

" USER COLORS "
"""""""""""""""
highlight User1  ctermbg=66      ctermfg=235    cterm=none
highlight User2  ctermbg=237     ctermfg=66     cterm=bold
highlight User5  ctermbg=7       ctermfg=235    cterm=bold
highlight User6  ctermbg=239     ctermfg=7      cterm=none
highlight User3  ctermbg=237     ctermfg=142    cterm=none
highlight User4  ctermbg=236     ctermfg=237    cterm=bold
highlight User7  ctermbg=239     ctermfg=15     cterm=bold
highlight User8  ctermbg=236     ctermfg=239    cterm=bold
highlight User9  ctermbg=236     ctermfg=15     cterm=bold

"""""""""""""""""
"   SEGMENTS    "
"""""""""""""""""

" LEFT SEGMENT "
""""""""""""""""
let $CUR_DIR="%1* %t %T %2*"               " current dir
" let $CUR_FILE_SZ="%3* %E %4*"       " current file size

" GIT SUPPORT "
"""""""""""""""
let $GIT="%3* %{system('sh ~/.config/vifm/scripts/GitStatus.sh')}%4*"

" SEPARATOR "
"""""""""""""
let $SEPARATOR="%="                 " middle separator

" RIGHT SEGMENT "
"""""""""""""""""
let $ATTR="%9* %A   %E "                 " file attributes
let $SPACE="%8*%7* %a "            " free space
let $DATE="%6*%5* %d "                 " date

" SET STATUSLINE "
""""""""""""""""""
execute 'set' 'statusline="' . $CUR_DIR . $GIT . $SEPARATOR . $ATTR . $SPACE . $DATE .'"'
