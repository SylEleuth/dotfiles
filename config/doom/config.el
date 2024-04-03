;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Eleuth"
      user-mail-address "Eleuth@is.me")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:

(setq doom-font (font-spec :family "JetBrains Mono Nerd Font" :size 14 :weight 'bold)
      doom-variable-pitch-font (font-spec :family "Ubuntu Nerd Font" :size 14)
      doom-big-font (font-spec :family "Hack Nerd Font" :size 24 :weight 'bold))

(custom-set-faces!
  '(font-lock-comment-face :slant italic)
  '(font-lock-keyword-face :slant italic))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-gruvbox)
;; (load-theme 'gruvbox t)

(after! doom-themes
  (setq doom-themes-enable-bold t
        doom-themes-enable-italic t))

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

(require 'powerline)
(powerline-default-theme)
(powerline-raw mode-line-mule-info nil 'l)

(setq display-line-numbers-type 'relative
      default-directory "~")

(setq-default show-trailing-whitespace t)

(global-auto-revert-mode t)

(setq centaur-tabs-style "alternate"
      centaur-tabs-height 10
      centaur-tabs-set-close-button nil
      centaur-tabs-set-icons t
      centaur-tabs-icon-scale-factor 0.75)

(map! :leader
      :desc "Open Treemacs" "-" #'treemacs)

(defvar buffer-expose-mode-map
  (let ((map (make-sparse-keymap)))
    (define-key map (kbd "<s-tab>") 'buffer-expose)
    (define-key map (kbd "<C-tab>") 'buffer-expose-no-stars)
    (define-key map (kbd "C-c <C-tab>") 'buffer-expose-current-mode)
    (define-key map (kbd "C-c C-m") 'buffer-expose-major-mode)
    (define-key map (kbd "C-c C-d") 'buffer-expose-dired-buffers)
    (define-key map (kbd "C-c C-*") 'buffer-expose-stars)
    map)
  "Mode map for command `buffer-expose-mode'.")

;; (with-eval-after-load 'evil-maps
;;   (define-key evil-motion-state-map (kbd "<C-k>") 'move-text-up)
;;   (define-key evil-motion-state-map (kbd "<C-j>") 'move-text-down))
;;   (define-key evil-motion-state-map (kbd ":") 'evil-repeat-find-char)
;;   (define-key evil-motion-state-map (kbd ";") 'evil-ex))

(global-set-key (kbd "<C-left>") 'previous-buffer)
(global-set-key (kbd "<C-right>") 'next-buffer)
(global-set-key (kbd "<S-left>") 'windmove-left)
(global-set-key (kbd "<S-right>") 'windmove-right)
(global-set-key (kbd "<S-down>") 'windmove-down)
(global-set-key (kbd "<S-up>") 'windmove-up)
(global-set-key (kbd "<C-k>") 'move-text-up)
(global-set-key (kbd "<C-j>") 'move-text-down)

(global-unset-key (kbd "M-<left>"))
(global-unset-key (kbd "M-<right>"))
