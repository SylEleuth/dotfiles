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
highlight User1  ctermbg=4       ctermfg=0      cterm=none
highlight User2  ctermbg=237     ctermfg=4      cterm=none
highlight User3  ctermbg=237     ctermfg=10     cterm=none
highlight User4  ctermbg=0       ctermfg=237    cterm=bold
highlight User5  ctermbg=7       ctermfg=0      cterm=bold
highlight User6  ctermbg=239     ctermfg=7      cterm=none
highlight User7  ctermbg=239     ctermfg=15     cterm=bold
highlight User8  ctermbg=237     ctermfg=239    cterm=bold
highlight User9  ctermbg=237     ctermfg=15     cterm=bold

"""""""""""""""""
"   SEGMENTS    "
"""""""""""""""""

" LEFT SEGMENT "
""""""""""""""""
let $CUR_DIR="%1* %t %2*"               " current dir
let $LINK="%3* %T %4*"                  " soft link to file or directory

" GIT SUPPORT "
"""""""""""""""
let $GIT="%3* %{system('sh ~/.config/vifm/scripts/GitStatus.sh')}%3*"

" SEPARATOR "
"""""""""""""
let $SEPARATOR="%="                      " middle separator

" RIGHT SEGMENT "
"""""""""""""""""
let $SIZE="%A (%o)"                        " file attributes
let $ATTR=" %4*%9* %E "                 " file size
let $SPACE="%8*%7* %a "                 " free space
let $DATE="%6*%5* %d "                  " date

" SET STATUSLINE "
""""""""""""""""""
" execute 'set' 'statusline="' . $CUR_DIR . $GIT . $LINK . $SEPARATOR . $ATTR . $SPACE . $DATE .'"'
execute 'set' 'statusline="' . $CUR_DIR . $LINK . $SEPARATOR . $SIZE . $ATTR . $SPACE . $DATE .'"'
