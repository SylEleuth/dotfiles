" SEPARATORS "
"""""""""""""""
let $L_B=""
let $L_T=""
let $R_B=""
let $R_T=""

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
" let $SIZE="%A (%o)"                      " file attributes
" let $ATTR=" %4*%2* %E "                 " file size
let $SPACE="%4*%6* %E %8* %6*%a "      " free space
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
set tabprefix=""
set tabsuffix=""
let $PREFIX="%8*%[%5*%C%] %6*%[%5*%C%]%N: "
let $SUFFIX="%4*%[%9*%C%]"
let $TAB="%6*%[%5*%C%]%n "

" colors for statusline only, can't use with tabline in the same time, not enough user hl groups
" let $PREFIX="%9*%[%5*%C%] %N: "
" let $SUFFIX="%9*%[%9*%C%]"
" let $TAB="%9*%n(%[%[%T{tree}%]%[{%c}%]@%]%p:t)"

execute 'set' 'tablabel="' . $PREFIX . $TAB . $SUFFIX . '"'
