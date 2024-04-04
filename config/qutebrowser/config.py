# pyright: reportUndefinedVariable=false
# type: ignore

config.load_autoconfig(False)
config.source("gruvbox.py")
config.source("bindings.py")

c.aliases = {
    "w": "session-save",
    "q": "quit",
    "wq": "quit --save",
    "ff": "spawn firefox {url}",
    "tor": "config-cycle -p content.proxy socks://localhost:9050/ system",
    "toroff": "set content.proxy system",
    "toron": "set content.proxy socks://localhost:9050",
    "zotero": "spawn --userscript zotero",
    "zotero_link": "hint links userscript zotero",
}
c.editor.encoding = "utf-8"
c.fonts.default_family = 'Ubuntu, "Hack Nerd Font", monospace'
c.tabs.max_width = -1
c.tabs.min_width = -1
c.auto_save.interval = 15000
c.auto_save.session = True
c.backend = "webengine"
c.completion.show = "auto"
c.completion.shrink = True
c.completion.use_best_match = True
c.completion.web_history.max_items = -1
c.confirm_quit = ["always"]
c.content.autoplay = False
c.content.cookies.accept = "no-3rdparty"
c.content.webrtc_ip_handling_policy = "default-public-interface-only"
c.content.site_specific_quirks.enabled = False
c.content.default_encoding = "utf-8"
c.content.dns_prefetch = True
c.content.geolocation = False
c.content.headers.accept_language = "en-US,en"
c.content.headers.do_not_track = True
c.content.blocking.enabled = True
c.content.blocking.hosts.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
]
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://easylist.to/easylist/fanboy-annoyance.txt",
    "https://easylist-downloads.adblockplus.org/easylistdutch.txt",
    "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",  # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt", \
    # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt", \
    # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt", \
    # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt", \
    # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt", \
    # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt" \
    "https://www.i-dont-care-about-cookies.eu/abp/",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
]
# c.content.javascript.clipboard = none
c.content.javascript.can_open_tabs_automatically = False
c.content.javascript.enabled = True
c.content.javascript.log = {
    "unknown": "debug",
    "info": "debug",
    "warning": "debug",
    "error": "debug",
}
c.content.javascript.modal_dialog = True
c.content.javascript.prompt = True
c.content.local_content_can_access_file_urls = True
c.content.local_content_can_access_remote_urls = False
c.content.local_storage = True
c.content.netrc_file = None
c.content.notifications.enabled = "ask"
c.content.pdfjs = False
c.content.plugins = False
c.content.print_element_backgrounds = True
c.content.private_browsing = False
c.content.proxy = "system"
c.content.user_stylesheets = None
c.content.webgl = True
c.content.xss_auditing = True
c.downloads.location.directory = "~/Downloads"
c.downloads.location.prompt = False
c.downloads.location.remember = True
c.downloads.location.suggestion = "path"
c.downloads.open_dispatcher = None
c.downloads.position = "bottom"
c.downloads.remove_finished = 1000
c.editor.command = ["nvim", "-e", "nvim '{}'"]
c.editor.encoding = "utf-8"
c.fonts.completion.entry = 'bold 10pt "Ubuntu"'
c.fonts.hints = 'bold 10pt "Ubuntu"'
c.fonts.keyhint = 'bold 10pt "Ubuntu"'
c.fonts.statusbar = 'bold 10pt "Ubuntu"'
c.fonts.tabs.selected = 'bold 10pt "Ubuntu"'
c.fonts.tabs.unselected = '10pt "Ubuntu"'
c.hints.chars = "qwerasdfzxcv"
c.scrolling.bar = "when-searching"
c.scrolling.smooth = True
c.spellcheck.languages = ["en-GB", "pl-PL"]
c.statusbar.show = "in-mode"
c.statusbar.position = "bottom"
c.statusbar.widgets = ["progress", "keypress", "url", "history"]
c.tabs.background = True
c.tabs.close_mouse_button = "middle"
c.tabs.favicons.scale = 1
c.tabs.favicons.show = "always"
c.tabs.indicator.padding = {"top": 2, "bottom": 2, "left": 0, "right": 4}
c.tabs.padding = {"top": 2, "bottom": 2, "left": 5, "right": 5}
c.tabs.last_close = "ignore"
c.tabs.mousewheel_switching = True
c.tabs.new_position.related = "next"
c.tabs.new_position.unrelated = "next"
c.tabs.position = "top"
c.tabs.select_on_remove = "last-used"
c.tabs.show = "multiple"
c.tabs.show_switching_delay = 800
c.tabs.tabs_are_windows = False
c.tabs.title.alignment = "center"
c.tabs.title.format = "{index}: {audio}{current_title}"
c.tabs.title.format_pinned = ""
c.tabs.width = "10%"
c.tabs.indicator.width = 0
c.tabs.wrap = True
c.url.auto_search = "naive"
c.url.default_page = "https://web.tabliss.io/"
c.url.incdec_segments = ["path", "query"]
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "w": "https://www.wikipedia.org/w/index.php?title=Special:Search&search={}",
    "g": "https://www.google.com/search?q=%{}",
    "y": "https://www.youtube.com/results?search_query={}",
    "m": "https://www.google.com/maps?q={}",
    "i": "https://www.imdb.com/find?s=all&q={}",
    "t": "https://twitter.com/search?q={}&f=user",
    "s": "https://stackexchange.com/search?q={}",
    "gh": "https://github.com/search?q={}",
    "r": "https://www.reddit.com/search/?q={}",
    "au": "https://aur.archlinux.org/packages/?O=0&K={}",
    "ar": "https://www.archlinux.org/packages/?sort=&q={}",
    "en": "https://translate.google.com/u/0/?sl=en&tl=pl&text={}%0A&op=translate",
    "pl": "https://translate.google.com/u/0/?sl=pl&tl=en&text={}%0A&op=translate",
    "wh": "https://www.wowhead.com/search?q={}",
    "e": "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}",
}
c.url.start_pages = "https://web.tabliss.io/"
c.url.yank_ignored_parameters = [
    "ref",
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
]
c.window.hide_decoration = False
c.window.title_format = "{perc}{current_title}{title_sep}qutebrowser"
c.zoom.default = "100%"
c.zoom.levels = [
    "25%",
    "33%",
    "50%",
    "67%",
    "75%",
    "90%",
    "100%",
    "110%",
    "125%",
    "150%",
    "175%",
    "200%",
    "250%",
    "300%",
    "400%",
    "500%",
]
c.zoom.mouse_divider = 512
