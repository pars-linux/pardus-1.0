
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Default configuration file for GNU/Emacs on Pardus ;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(setq column-number-mode t)		; show column numbers below

(display-time-mode t)			; display time below

(show-paren-mode t)			; show parenthesis

(transient-mark-mode t)			; show mark visually...

;; (setq make-backup-files nil)		; no nasty back-up files

(setq show-trailing-whitespace t)	; show whitespaces at the end of the line

(setq frame-title-format "%b (%m)")	; descriptive frame title "filename (mode)"

(setq scroll-step 1)			; scroll one line at a time

;; use ibufferr by default
(global-set-key (kbd "C-x C-b") 'ibuffer)
(autoload 'ibuffer "ibuffer" "List buffers." t)


