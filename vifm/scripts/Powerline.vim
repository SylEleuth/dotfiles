" SEPARATORS "
"""""""""""""""
let L_B=""
let L_T=""
let R_B=""
let R_T=""

" USER COLORS "
"""""""""""""""
highlight User1  ctermbg=237     ctermfg=5      cterm=italic
highlight User2  ctermbg=237     ctermfg=4      cterm=none
highlight User3  ctermbg=237     ctermfg=10     cterm=none
highlight User4  ctermbg=0       ctermfg=237    cterm=none
highlight User5  ctermbg=7       ctermfg=0      cterm=none
highlight User6  ctermbg=237     ctermfg=7      cterm=none
highlight User7  ctermbg=237     ctermfg=15     cterm=none
highlight User8  ctermbg=237     ctermfg=0      cterm=none
highlight User9  ctermbg=0       ctermfg=7      cterm=none
highlight User20 ctermbg=9       ctermfg=0      cterm=none

" more colors for statusline only
" highlight User1  ctermbg=4       ctermfg=0      cterm=none
" highlight User2  ctermbg=237     ctermfg=4      cterm=none
" highlight User3  ctermbg=237     ctermfg=10     cterm=none
" highlight User4  ctermbg=0       ctermfg=237    cterm=bold
" highlight User5  ctermbg=7       ctermfg=0      cterm=bold
" highlight User6  ctermbg=237     ctermfg=7      cterm=none
" highlight User7  ctermbg=237     ctermfg=15     cterm=bold
" highlight User8  ctermbg=237     ctermfg=237    cterm=bold
" highlight User9  ctermbg=0       ctermfg=7      cterm=bold

" LEFT SEGMENT "
""""""""""""""""
let $CUR_DIR="%5* %t %6*"               " current dir
" let $LINK="%3* %T %4*"                  " soft link to file or directory
let $LINK="%1* %T %4*"                  " soft link to file or directory

" GIT SUPPORT "
"""""""""""""""
let $GIT="%3* %{system('sh ~/.config/vifm/scripts/GitStatus.sh')}%3*"

" SEPARATOR "
"""""""""""""
let $SEPARATOR="%="                      " middle separator

" RIGHT SEGMENT "
"""""""""""""""""
" let $SIZE="%A (%o)"                        " file attributes
" let $ATTR=" %4*%2* %E "                 " file size
let $SPACE="%4*%6* %E  %a "                 " free space
let $DATE="%6*%5* %d "                  " date
" let $DATE="%6*%5* %d "                  " date

" SET STATUSLINE "
""""""""""""""""""
" execute 'set' 'statusline="' . $CUR_DIR . $GIT . $LINK . $SEPARATOR . $ATTR . $SPACE . $DATE .'"'
execute 'set' 'statusline="' . $CUR_DIR . $LINK . $SEPARATOR . $SIZE . $ATTR . $SPACE . $DATE .'"'


" SET RULERFORMAT "
"""""""""""""""""""

let $RULER="%2l/%S%[ +%x%] "
execute 'set' 'rulerformat="' . $RULER . '"'


" SET TABLINE "
"""""""""""""""
let $PREFIX="%8*%[%5*%C%] %6*%[%5*%C%]%N: "
let $SUFFIX="%4*%[%9*%C%]"
let $TAB="%6*%[%5*%C%]%n "

" colors for statusline only, can't use with tabline in the same time, not enough user hl groups
" let $PREFIX="%9*%[%5*%C%] %N: "
" let $SUFFIX="%9*%[%9*%C%]"
" let $TAB="%9*%n(%[%[%T{tree}%]%[{%c}%]@%]%p:t)"

execute 'set' 'tablabel="' . $PREFIX . $TAB . $SUFFIX . '"'
