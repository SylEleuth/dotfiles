nnoremap <silent> w : if &quickview && !layoutis('only')
                   \|     view
                   \| else
                   \|     if layoutis('only')
                   \|         if &lines + 50 < &columns | vsplit | else | split | endif
                   \|     endif
                   \|     view!
                   \|     execute 'qnoremap w q:view|only|qunmap w<lt>cr>'
                   \|     execute 'wincmd w'
                   \| endif
                   \| <cr>
