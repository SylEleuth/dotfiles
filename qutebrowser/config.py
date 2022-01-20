config.load_autoconfig(False)

# import dracula.draw

# # Load existing settings made via :set
# config.load_autoconfig()

# dracula.draw.blood(c, {
#     'spacing': {
#         'vertical': 6,
#         'horizontal': 8
#     }
# })

c.aliases = {'w': 'session-save',
             'q': 'quit',
             'wq': 'quit --save',
             'ff': 'spawn firefox {url}',
             'tor': 'config-cycle -p content.proxy socks://localhost:9050/ system',
             'toroff': 'set content.proxy system',
             'toron': 'set content.proxy socks://localhost:9050',
             'zotero': 'spawn --userscript zotero',
             'zotero_link': 'hint links userscript zotero'
             }


c.editor.encoding = 'utf-8'
c.fonts.default_family = '"Hack Nerd Font", "FantasqueSansmono Nerd Font", "Roboto", Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

c.content.autoplay = False

c.tabs.max_width = -1
c.tabs.min_width = -1

# How often (in milliseconds) to auto-save config/cookies/etc.
# Type: Int
c.auto_save.interval = 15000

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

#   - webengine: Use QtWebEngine (based on Chromium)
#   - webkit: Use QtWebKit (based on WebKit, similar to Safari)
c.backend = 'webengine'

# # Type: Dict
# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>',
#                            '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

# # Background color of the completion widget category headers.
# # Type: QssColor
# c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'

# # Bottom border color of the completion widget category headers.
# # Type: QssColor
# c.colors.completion.category.border.bottom = 'black'

# # Top border color of the completion widget category headers.
# # Type: QssColor
# c.colors.completion.category.border.top = 'black'

# # Foreground color of completion widget category headers.
# # Type: QtColor
# c.colors.completion.category.fg = 'white'

# # Background color of the completion widget for even rows.
# # Type: QssColor
# c.colors.completion.even.bg = '#333333'

# # Text color of the completion widget.
# # Type: QtColor
# c.colors.completion.fg = 'white'

# # Background color of the selected completion item.
# # Type: QssColor
# c.colors.completion.item.selected.bg = '#e8c000'

# # Bottom border color of the selected completion item.
# # Type: QssColor
# c.colors.completion.item.selected.border.bottom = '#bbbb00'

# # Top border color of the completion widget category headers.
# # Type: QssColor
# c.colors.completion.item.selected.border.top = '#bbbb00'

# # Foreground color of the selected completion item.
# # Type: QtColor
# c.colors.completion.item.selected.fg = 'black'

# # Foreground color of the matched text in the completion.
# # Type: QssColor
# c.colors.completion.match.fg = '#ff4444'

# # Background color of the completion widget for odd rows.
# # Type: QssColor
# c.colors.completion.odd.bg = '#444444'

# # Color of the scrollbar in completion view
# # Type: QssColor
# c.colors.completion.scrollbar.bg = '#333333'

# # Color of the scrollbar handle in completion view.
# # Type: QssColor
# c.colors.completion.scrollbar.fg = 'white'

# # Background color for the download bar.
# # Type: QssColor
# c.colors.downloads.bar.bg = 'black'

# # Background color for downloads with errors.
# # Type: QtColor
# c.colors.downloads.error.bg = 'red'

# # Foreground color for downloads with errors.
# # Type: QtColor
# c.colors.downloads.error.fg = 'white'

# # Color gradient start for download backgrounds.
# # Type: QtColor
# c.colors.downloads.start.bg = '#0000aa'

# # Color gradient start for download text.
# # Type: QtColor
# c.colors.downloads.start.fg = 'white'

# # Color gradient stop for download backgrounds.
# # Type: QtColor
# c.colors.downloads.stop.bg = '#00aa00'

# # Color gradient end for download text.
# # Type: QtColor
# c.colors.downloads.stop.fg = 'white'

# # Color gradient interpolation system for download backgrounds.
# # Type: ColorSystem
# # Valid values:
# #   - rgb: Interpolate in the RGB color system.
# #   - hsv: Interpolate in the HSV color system.
# #   - hsl: Interpolate in the HSL color system.
# #   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'

# # Color gradient interpolation system for download text.
# # Type: ColorSystem
# # Valid values:
# #   - rgb: Interpolate in the RGB color system.
# #   - hsv: Interpolate in the HSV color system.
# #   - hsl: Interpolate in the HSL color system.
# #   - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

# # Background color for hints. Note that you can use a `rgba(...)` value
# # for transparency.
# # Type: QssColor
# c.colors.hints.bg = 'rgba(0,0,0,128)'

# # Font color for hints.
# # Type: QssColor
# c.colors.hints.fg = 'white'

# # Font color for the matched part of hints.
# # Type: QssColor
# c.colors.hints.match.fg = 'rgba(0,0,0,128)'

# # Background color of the keyhint widget.
# # Type: QssColor
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

# # Text color for the keyhint widget.
# # Type: QssColor
# c.colors.keyhint.fg = '#FFFFFF'

# # Highlight color for keys to complete the current keychain.
# # Type: QssColor
# c.colors.keyhint.suffix.fg = '#FFFF00'

# # Background color of an error message.
# # Type: QssColor
# c.colors.messages.error.bg = 'red'

# # Border color of an error message.
# # Type: QssColor
# c.colors.messages.error.border = '#bb0000'

# # Foreground color of an error message.
# # Type: QssColor
# c.colors.messages.error.fg = 'white'

# # Background color of an info message.
# # Type: QssColor
# c.colors.messages.info.bg = 'black'

# # Border color of an info message.
# # Type: QssColor
# c.colors.messages.info.border = '#333333'

# # Foreground color an info message.
# # Type: QssColor
# c.colors.messages.info.fg = 'white'

# # Background color of a warning message.
# # Type: QssColor
# c.colors.messages.warning.bg = 'darkorange'

# # Border color of a warning message.
# # Type: QssColor
# c.colors.messages.warning.border = '#d47300'

# # Foreground color a warning message.
# # Type: QssColor
# c.colors.messages.warning.fg = 'white'

# # Background color for prompts.
# # Type: QssColor
# c.colors.prompts.bg = '#444444'

# # Border used around UI elements in prompts.
# # Type: String
# c.colors.prompts.border = '1px solid gray'

# # Foreground color for prompts.
# # Type: QssColor
# c.colors.prompts.fg = 'white'

# # Background color for the selected item in filename prompts.
# # Type: QssColor
# c.colors.prompts.selected.bg = 'grey'

# # Background color of the statusbar in caret mode.
# # Type: QssColor
# c.colors.statusbar.caret.bg = 'purple'

# # Foreground color of the statusbar in caret mode.
# # Type: QssColor
# c.colors.statusbar.caret.fg = 'white'

# # Background color of the statusbar in caret mode with a selection.
# # Type: QssColor
# c.colors.statusbar.caret.selection.bg = '#a12dff'

# # Foreground color of the statusbar in caret mode with a selection.
# # Type: QssColor
# c.colors.statusbar.caret.selection.fg = 'white'

# # Background color of the statusbar in command mode.
# # Type: QssColor
# c.colors.statusbar.command.bg = 'black'

# # Foreground color of the statusbar in command mode.
# # Type: QssColor
# c.colors.statusbar.command.fg = 'white'

# # Background color of the statusbar in private browsing + command mode.
# # Type: QssColor
# c.colors.statusbar.command.private.bg = 'grey'

# # Foreground color of the statusbar in private browsing + command mode.
# # Type: QssColor
# c.colors.statusbar.command.private.fg = 'white'

# # Background color of the statusbar in insert mode.
# # Type: QssColor
# c.colors.statusbar.insert.bg = 'darkgreen'

# # Foreground color of the statusbar in insert mode.
# # Type: QssColor
# c.colors.statusbar.insert.fg = 'white'

# # Background color of the statusbar.
# # Type: QssColor
# c.colors.statusbar.normal.bg = 'black'

# # Foreground color of the statusbar.
# # Type: QssColor
# c.colors.statusbar.normal.fg = 'white'

# # Background color of the statusbar in private browsing mode.
# # Type: QssColor
# c.colors.statusbar.private.bg = '#666666'

# # Foreground color of the statusbar in private browsing mode.
# # Type: QssColor
# c.colors.statusbar.private.fg = 'white'

# # Background color of the progress bar.
# # Type: QssColor
# c.colors.statusbar.progress.bg = 'white'

# # Foreground color of the URL in the statusbar on error.
# # Type: QssColor
# c.colors.statusbar.url.error.fg = 'orange'

# # Default foreground color of the URL in the statusbar.
# # Type: QssColor
# c.colors.statusbar.url.fg = 'white'

# # Foreground color of the URL in the statusbar for hovered links.
# # Type: QssColor
# c.colors.statusbar.url.hover.fg = 'aqua'

# # Foreground color of the URL in the statusbar on successful load
# # (http).
# # Type: QssColor
# c.colors.statusbar.url.success.http.fg = 'white'

# # Foreground color of the URL in the statusbar on successful load
# # (https).
# # Type: QssColor
# c.colors.statusbar.url.success.https.fg = 'lime'

# # Foreground color of the URL in the statusbar when there's a warning.
# # Type: QssColor
# c.colors.statusbar.url.warn.fg = 'yellow'

# # Background color of the tab bar.
# # Type: QtColor
# c.colors.tabs.bar.bg = '#555555'

# # Background color of unselected even tabs.
# # Type: QtColor
# c.colors.tabs.even.bg = 'darkgrey'

# # Foreground color of unselected even tabs.
# # Type: QtColor
# c.colors.tabs.even.fg = 'white'

# # Color for the tab indicator on errors.
# # Type: QtColor
# c.colors.tabs.indicator.error = '#ff0000'

# # Color gradient start for the tab indicator.
# # Type: QtColor
# c.colors.tabs.indicator.start = '#0000aa'

# # Color gradient end for the tab indicator.
# # Type: QtColor
# c.colors.tabs.indicator.stop = '#00aa00'

# # Color gradient interpolation system for the tab indicator.
# # Type: ColorSystem
# # Valid values:
# #   - rgb: Interpolate in the RGB color system.
# #   - hsv: Interpolate in the HSV color system.
# #   - hsl: Interpolate in the HSL color system.
# #   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

# # Background color of unselected odd tabs.
# # Type: QtColor
# c.colors.tabs.odd.bg = 'grey'

# # Foreground color of unselected odd tabs.
# # Type: QtColor
# c.colors.tabs.odd.fg = 'white'

# # Background color of selected even tabs.
# # Type: QtColor
# c.colors.tabs.selected.even.bg = 'black'

# # Foreground color of selected even tabs.
# # Type: QtColor
# c.colors.tabs.selected.even.fg = 'white'

# # Background color of selected odd tabs.
# # Type: QtColor
# c.colors.tabs.selected.odd.bg = 'black'

# # Foreground color of selected odd tabs.
# # Type: QtColor
# c.colors.tabs.selected.odd.fg = 'white'

# # Background color for webpages if unset (or empty to use the theme's
# # color)
# # Type: QtColor
# c.colors.webpage.bg = 'white'

# # How many commands to save in the command history. 0: no history / -1:
# # unlimited
# # Type: Int
# c.completion.cmd_history_max_items = 100

# The height of the completion, in px or as percentage of the window.
# Type: PercOrInt
c.completion.height = '30%'

# # Move on to the next part when there's only one possible completion
# # left.
# # Type: Bool
# c.completion.quick = True

# # Padding of scrollbar handle in the completion window (in px).
# # Type: Int
# c.completion.scrollbar.padding = 2

# # Width of the scrollbar in the completion window (in px).
# # Type: Int
# c.completion.scrollbar.width = 12

# When to show the autocompletion window.
# Type: String
# Valid values:
#   - always: Whenever a completion is available.
#   - auto: Whenever a completion is requested.
#   - never: Never.
c.completion.show = 'auto'

# Shrink the completion to be smaller than the configured size if there
# are no scrollbars.
# Type: Bool
c.completion.shrink = False

# How to format timestamps (e.g. for the history completion).
# Type: TimestampTemplate
# c.completion.timestamp_format = '%Y-%m-%d'

# How many URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history.max_items = -1

# Whether quitting the application requires a confirmation.
# Type: ConfirmQuit
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ['always']

# Whether support for the HTML 5 web application cache feature is
# enabled. An application cache acts like an HTTP cache in some sense.
# For documents that use the application cache via JavaScript, the
# loader engine will first ask the application cache for the contents,
# before hitting the network.
# Type: Bool

# The maximum number of pages to hold in the global memory page cache.
# The Page Cache allows for a nicer user experience when navigating
# forth or back to pages in the forward/back history, by pausing and
# resuming up to _n_ pages. For more information about the feature,
# please refer to: http://webkit.org/blog/427/webkit-page-cache-i-the-
# basics/
# Type: Int
# c.content.cache.maximum_pages = 0

# Size of the HTTP network cache. Null to use the default value.
# Type: Int
# c.content.cache.size = None

# Control which cookies to accept.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain.
#   - never: Don't accept cookies at all.
c.content.cookies.accept = 'no-3rdparty'

# Store cookies. Note this option needs a restart with QtWebEngine on Qt
# < 5.9.
# Type: Bool
# c.content.cookies.store = True

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
c.content.default_encoding = 'utf-8'

# Try to pre-fetch DNS entries to speed up browsing.
# Type: Bool
c.content.dns_prefetch = True

# Expand each subframe to its contents. This will flatten all the frames
# to become one scrollable page.
# Type: Bool
# c.content.frame_flattening = False

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.geolocation = False

# Value to send in the `Accept-Language` header.
# Type: String
c.content.headers.accept_language = 'en-US,en'

# Set custom headers for qutebrowser HTTP requests.
# Type: Dict
# c.content.headers.custom = {}

# Value to send in the `DNT` header. When this is set to true,
# qutebrowser asks websites to not track your identity. If set to null,
# the DNT header is not sent at all.
# Type: Bool
c.content.headers.do_not_track = True

# Send the Referer header. The Referer header tells websites from which
# website you were coming from when visting them.
# Type: String
# Valid values:
#   - always: Always send the Referer.
#   - never: Never send the Referer. This is not recommended, as some sites may break.
#   - same-domain: Only send the Referer for the same domain. This will stooill protect your privacy, but shouldn't break any sites.
# c.content.headers.referer = 'same-domain'

# User agent to send. Unset to send the default.
# Type: String
# c.content.headers.user_agent = None

# Whether host blocking is enabled.
# Type: Bool
c.content.blocking.enabled = True

c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.blocking.method = 'both'

# List of URLs of lists which contain hosts to block.  The file can be
# in one of the following formats:  - An `/etc/hosts`-like file - One
# host per line - A zip-file of any of the above, with either only one
# file, or a file named   `hosts` (with any extension).
# Type: List of Url
c.content.blocking.adblock.lists = [ \
        "https://easylist.to/easylist/easylist.txt", \
        "https://easylist.to/easylist/easyprivacy.txt", \
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt", \
        "https://easylist.to/easylist/fanboy-annoyance.txt", \
        'https://easylist-downloads.adblockplus.org/easylistdutch.txt', \
        'https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt', \
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt", \
        # "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt" \
        'https://www.i-dont-care-about-cookies.eu/abp/', \
        'https://secure.fanboy.co.nz/fanboy-cookiemonster.txt' \
        ]

# List of domains that should always be loaded, despite being ad-
# blocked. Domains may contain * and ? wildcards and are otherwise
# required to exactly match the requested domain. Local domains are
# always exempt from hostblocking.
# Type: List of String
# c.content.host_blocking.whitelist = ['']

# Enable or disable hyperlink auditing (`<a ping>`).
# Type: Bool
# c.content.hyperlink_auditing = False

# Whether images are automatically loaded in web pages.
# Type: Bool
# c.content.images = True

# Show javascript alerts.
# Type: Bool
# c.content.javascript.alert = True

# Whether JavaScript can read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
# Type: Bool
c.content.javascript.can_access_clipboard = False

# Whether JavaScript can close tabs.
# Type: Bool
# c.content.javascript.can_close_tabs = False

# Whether JavaScript can open new tabs without user interaction.
# Type: Bool
c.content.javascript.can_open_tabs_automatically = False

# Enables or disables JavaScript.
# Type: Bool
c.content.javascript.enabled = True

# Log levels to use for JavaScript console logging messages. When a
# JavaScript message with the level given in the dictionary key is
# logged, the corresponding dictionary value selects the qutebrowser
# logger to use. On QtWebKit, the "unknown" setting is always used.
# Type: Dict
c.content.javascript.log = {'unknown': 'debug',
                            'info': 'debug', 'warning': 'debug', 'error': 'debug'}

# Use the standard JavaScript modal dialog for `alert()` and `confirm()`
# Type: Bool
c.content.javascript.modal_dialog = True

# Show javascript prompts.
# Type: Bool
c.content.javascript.prompt = True

# Whether locally loaded documents are allowed to access other local
# urls.
# Type: Bool
c.content.local_content_can_access_file_urls = True

# Whether locally loaded documents are allowed to access remote urls.
# Type: Bool
c.content.local_content_can_access_remote_urls = False

# Whether support for HTML 5 local storage and Web SQL is enabled.
# Type: Bool
c.content.local_storage = True

# Allow websites to record audio/video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# c.content.media_capture = False

# Location of a netrc-file for HTTP authentication. If unset, `~/.netrc`
# is used.
# Type: File
c.content.netrc_file = None

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.notifications.enabled = 'ask'

# Enable pdf.js to view PDF files in the browser. Note that the files
# can still be downloaded by clicking the download button in the pdf.js
# viewer.
# Type: Bool
c.content.pdfjs = False

# Enables or disables plugins in Web pages.
# Type: Bool
c.content.plugins = False

# Whether the background color and images are also drawn when the page
# is printed.
# Type: Bool
c.content.print_element_backgrounds = True

# Open new windows in private browsing mode which does not record
# visited pages.
# Type: Bool
c.content.private_browsing = False

# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Type: Proxy
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don't use any proxy
c.content.proxy = 'system'

# Send DNS requests over the configured proxy.
# Type: Bool
# c.content.proxy_dns_requests = True

# Validate SSL handshakes.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# c.content.ssl_strict = False

# A list of user stylesheet filenames to use.
# Type: List of File, or File
c.content.user_stylesheets = None

# Enables or disables WebGL.
# Type: Bool
c.content.webgl = True

# Whether load requests should be monitored for cross-site scripting
# attempts. Suspicious scripts will be blocked and reported in the
# inspector's JavaScript console. Enabling this feature might have an
# impact on performance.
# Type: Bool
c.content.xss_auditing = True

# The directory to save downloads to. If unset, a sensible os-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '~/Downloads'

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
# Type: Bool
c.downloads.location.prompt = False

# Remember the last used download directory.
# Type: Bool
c.downloads.location.remember = True

# What to display in the download filename input.
# Type: String
# Valid values:
#   - path: Show only the download path.
#   - filename: Show only download filename.
#   - both: Show download path and filename.
c.downloads.location.suggestion = 'path'

# The default program used to open downloads. If null, the default
# internal handler is used. Any `{}` in the string will be expanded to
# the filename, else the filename will be appended.
# Type: String
c.downloads.open_dispatcher = None

# Where to show the downloaded files.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.downloads.position = 'top'

# Number of milliseconds to wait before removing finished downloads. If
# set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = 1000

# The editor (and arguments) to use for the `open-editor` command. `{}`
# gets replaced by the filename of the file to be edited.
# Type: ShellCommand
c.editor.command = ['termite',  '-e', "vim '{}'"]

# Encoding to use for the editor.
# Type: Encoding
c.editor.encoding = 'utf-8'

# # Font used in the completion categories.
# # Type: Font
# c.fonts.completion.category = 'bold 12pt monospace'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = 'bold 10pt monospace'

# # Font used for the debugging console.
# # Type: QtFont
# c.fonts.debug_console = '10pt monospace'

# # Font used for the downloadbar.
# # Type: Font
# c.fonts.downloads = '10pt monospace'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt monospace'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = 'bold 10pt monospace'

# # Font used for error messages.
# # Type: Font
# c.fonts.messages.error = '10pt monospace'

# # Font used for info messages.
# # Type: Font
# c.fonts.messages.info = '10pt monospace'

# # Font used for warning messages.
# # Type: Font
# c.fonts.messages.warning = '10pt monospace'

# # Font used for prompts.
# # Type: Font
# c.fonts.prompts = '10pt monospace'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = 'bold 10pt monospace'

c.fonts.tabs.selected = 'bold 10pt "Ubuntu"'
c.fonts.tabs.unselected = '10pt "Ubuntu"'

# Chars used for hint strings.
c.hints.chars = "qwerasdfzxcv"

# # Font family for cursive fonts.
# # Type: FontFamily
# c.fonts.web.family.cursive = ''

# # Font family for fantasy fonts.
# # Type: FontFamily
# c.fonts.web.family.fantasy = ''

# # Font family for fixed fonts.
# # Type: FontFamily
# c.fonts.web.family.fixed = ''

# # Font family for sans-serif fonts.
# # Type: FontFamily
# c.fonts.web.family.sans_serif = ''

# # Font family for serif fonts.
# # Type: FontFamily
# c.fonts.web.family.serif = ''

# # Font family for standard fonts.
# # Type: FontFamily
# c.fonts.web.family.standard = ''

# # The default font size for regular text.
# # Type: Int
# c.fonts.web.size.default = 16

# # The default font size for fixed-pitch text.
# # Type: Int
# c.fonts.web.size.default_fixed = 13

# # The hard minimum font size.
# # Type: Int
# c.fonts.web.size.minimum = 0

# # The minimum logical font size that is applied when zooming out.
# # Type: Int
# c.fonts.web.size.minimum_logical = 6

# # Controls when a hint can be automatically followed without pressing
# # Enter.
# # Type: String
# # Valid values:
# #   - always: Auto-follow whenever there is only a single hint on a page.
# #   - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
# #   - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element's text (only in number mode).
# #   - never: The user will always need to press Enter to follow a hint.
# c.hints.auto_follow = 'unique-match'

# # A timeout (in milliseconds) to ignore normal-mode key bindings after a
# # successful auto-follow.
# # Type: Int
# c.hints.auto_follow_timeout = 0

# # CSS border value for hints.
# # Type: String
# c.hints.border = '1px solid black'

# # Chars used for hint strings.
# # Type: UniqueCharString
# c.hints.chars = 'tsrn'

# # The dictionary file to be used by the word hints.
# # Type: File
# c.hints.dictionary = '/usr/share/dict/words'

# # Which implementation to use to find elements to hint.
# # Type: String
# # Valid values:
# #   - javascript: Better but slower
# #   - python: Slightly worse but faster
# c.hints.find_implementation = 'python'

# # Hide unmatched hints in rapid mode.
# # Type: Bool
# c.hints.hide_unmatched_rapid_hints = True

# # Minimum number of chars used for hint strings.
# # Type: Int
# c.hints.min_chars = 1

# # Mode to use for hints.
# # Type: String
# # Valid values:
# #   - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
# #   - letter: Use the chars in the `hints.chars` setting.
# #   - word: Use hints words based on the html elements and the extra words.
# c.hints.mode = 'letter'

# # A comma-separated list of regexes to use for 'next' links.
# # Type: List of Regex
# c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b',
#                         '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

# # A comma-separated list of regexes to use for 'prev' links.
# # Type: List of Regex
# c.hints.prev_regexes = [
#     '\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']

# # Scatter hint key chains (like Vimium) or not (like dwb). Ignored for
# # number hints.
# # Type: Bool
# c.hints.scatter = False

# # Make chars in hint strings uppercase.
# # Type: Bool
# c.hints.uppercase = False

# # The maximum time in minutes between two history items for them to be
# # considered being from the same browsing session. Items with less time
# # between them are grouped when being displayed in `:history`. Use -1 to
# # disable separation.
# # Type: Int
# c.history_gap_interval = 30

# # Find text on a page case-insensitively.
# # Type: String
# # Valid values:
# #   - always: Search case-insensitively
# #   - never: Search case-sensitively
# #   - smart: Search case-sensitively if there are capital chars
# c.search.ignore_case = 'smart'

# # Forward unbound keys to the webview in normal mode.
# # Type: String
# # Valid values:
# #   - all: Forward all unbound keys.
# #   - auto: Forward unbound non-alphanumeric keys.
# #   - none: Don't forward any keys.
# c.input.forward_unbound_keys = 'auto'

# # Leave insert mode if a non-editable element is clicked.
# # Type: Bool
# c.input.insert_mode.auto_leave = True

# # Automatically enter insert mode if an editable element is focused
# # after loading the page.
# # Type: Bool
# c.input.insert_mode.auto_load = False

# # Switch to insert mode when clicking flash and other plugins.
# # Type: Bool
# c.input.insert_mode.plugins = False

# # Include hyperlinks in the keyboard focus chain when tabbing.
# # Type: Bool
# c.input.links_included_in_focus_chain = True

# # Timeout (in milliseconds) for partially typed key bindings. If the
# # current input forms only partial matches, the keystring will be
# # cleared after this time.
# # Type: Int
# c.input.partial_timeout = 5000

# # Enable Opera-like mouse rocker gestures. This disables the context
# # menu.
# # Type: Bool
# c.input.rocker_gestures = False

# # Enable Spatial Navigation. Spatial navigation consists in the ability
# # to navigate between focusable elements in a Web page, such as
# # hyperlinks and form controls, by using Left, Right, Up and Down arrow
# # keys. For example, if a user presses the Right key, heuristics
# # determine whether there is an element he might be trying to reach
# # towards the right and which element he probably wants.
# # Type: Bool
# c.input.spatial_navigation = False

# # Keychains that shouldn't be shown in the keyhint dialog. Globs are
# # supported, so `;*` will blacklist all keychains starting with `;`. Use
# # `*` to disable keyhints.
# # Type: List of String
# c.keyhint.blacklist = []

# # Time from pressing a key to seeing the keyhint dialog (ms).
# # Type: Int
# c.keyhint.delay = 500

# # Time (in ms) to show messages in the statusbar for. Set to 0 to never
# # clear messages.
# # Type: Int
# c.messages.timeout = 2000

# # How to open links in an existing instance if a new one is launched.
# # This happens when e.g. opening a link from a terminal. See
# # `new_instance_open_target_window` to customize in which window the
# # link is opened in.
# # Type: String
# # Valid values:
# #   - tab: Open a new tab in the existing window and activate the window.
# #   - tab-bg: Open a new background tab in the existing window and activate the window.
# #   - tab-silent: Open a new tab in the existing window without activating the window.
# #   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
# #   - window: Open in a new window.
# c.new_instance_open_target = 'tab'

# # Which window to choose when opening links as new tabs. When
# # `new_instance_open_target` is not set to `window`, this is ignored.
# # Type: String
# # Valid values:
# #   - first-opened: Open new tabs in the first (oldest) opened window.
# #   - last-opened: Open new tabs in the last (newest) opened window.
# #   - last-focused: Open new tabs in the most recently focused window.
# #   - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

# # Show a filebrowser in upload/download prompts.
# # Type: Bool
# c.prompt.filebrowser = True

# # The rounding radius for the edges of prompts.
# # Type: Int
# c.prompt.radius = 8

# # Additional arguments to pass to Qt, without leading `--`. With
# # QtWebEngine, some Chromium arguments (see
# # https://peter.sh/experiments/chromium-command-line-switches/ for a
# # list) will work. This setting requires a restart.
# # Type: List of String
# c.qt.args = []

# # Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
# # environment variable and is useful to force using the XCB plugin when
# # running QtWebEngine on Wayland.
# # Type: String
# c.qt.force_platform = None

# # Force software rendering for QtWebEngine. This is needed for
# # QtWebEngine to work with Nouveau drivers. This setting requires a
# # restart.
# # Type: Bool
# c.qt.force_software_rendering = "none"

# Show a scrollbar.
# Type: Bool
c.scrolling.bar = "when-searching"

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# The name of the session to save by default. If this is set to null,
# the session which was last loaded is saved.
# Type: SessionName
# c.session.default_name = None

# Spell checking languages. You can check for available languages and
# install dictionaries using scripts/install_dict.py. Run the script
# with -h/--help for instructions.
# Type: List of String
# Valid values:
#   - af-ZA: Afrikaans (South Africa)
#   - bg-BG: Bulgarian (Bulgaria)
#   - ca-ES: Catalan (Spain)
#   - cs-CZ: Czech (Czech Republic)
#   - da-DK: Danish (Denmark)
#   - de-DE: German (Germany)
#   - el-GR: Greek (Greece)
#   - en-CA: English (Canada)
#   - en-GB: English (United Kingdom)
#   - en-US: English (United States)
#   - es-ES: Spanish (Spain)
#   - et-EE: Estonian (Estonia)
#   - fa-IR: Farsi (Iran)
#   - fo-FO: Faroese (Faroe Islands)
#   - fr-FR: French (France)
#   - he-IL: Hebrew (Israel)
#   - hi-IN: Hindi (India)
#   - hr-HR: Croatian (Croatia)
#   - hu-HU: Hungarian (Hungary)
#   - id-ID: Indonesian (Indonesia)
#   - it-IT: Italian (Italy)
#   - ko: Korean
#   - lt-LT: Lithuanian (Lithuania)
#   - lv-LV: Latvian (Latvia)
#   - nb-NO: Norwegian (Norway)
#   - nl-NL: Dutch (Netherlands)
#   - pl-PL: Polish (Poland)
#   - pt-BR: Portuguese (Brazil)
#   - pt-PT: Portuguese (Portugal)
#   - ro-RO: Romanian (Romania)
#   - ru-RU: Russian (Russia)
#   - sh: Serbo-Croatian
#   - sk-SK: Slovak (Slovakia)
#   - sl-SI: Slovenian (Slovenia)
#   - sq: Albanian
#   - sr: Serbian
#   - sv-SE: Swedish (Sweden)
#   - ta-IN: Tamil (India)
#   - tg-TG: Tajik (Tajikistan)
#   - tr-TR: Turkish (Turkey)
#   - uk-UA: Ukrainian (Ukraine)
#   - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = ["en-GB", "pl-PL"]

# Hide the statusbar unless a message is shown.
# Type: Bool
# c.statusbar.hide = False

# The position of the status bar.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.statusbar.position = 'bottom'

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# On which mouse button to close tabs.
# Type: String
# Valid values:
#   - right: Close tabs on right-click.
#   - middle: Close tabs on middle-click.
#   - none: Don't close tabs using the mouse.
c.tabs.close_mouse_button = 'middle'

# Scaling for favicons in the tab bar. The tab size is unchanged, so big
# favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1

# Show favicons in the tab bar.
# Type: Bool
c.tabs.favicons.show = 'always'

# Padding for tab indicators
# Type: Padding
c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

# Behavior when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'ignore'

# Switch between tabs using the mouse wheel.
# Type: Bool
c.tabs.mousewheel_switching = True

# How new tabs opened from another tab are positioned.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.related = 'next'

# How new tabs which aren't opened from another tab are positioned.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.unrelated = 'next'

# Padding around text for tabs
# Type: Padding
c.tabs.padding = {'top': 2, 'bottom': 2, 'left': 5, 'right': 5}

# The position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'last-used'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# Time to show the tab bar before hiding it when tabs.show is set to
# 'switching'.
# Type: Int
c.tabs.show_switching_delay = 800

# Open a new window for every tab.
# Type: Bool
c.tabs.tabs_are_windows = False

# Alignment of the text inside of tabs.
# Type: TextAlignment
# Valid values:
#   - left
#   - right
#   - center
c.tabs.title.alignment = 'center'

# The format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: The percentage as a string like `[10%]`. *
# `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
# the current web page * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: The index of this tab. * `{id}`:
# The internal tab ID of this tab. * `{scroll_pos}`: The page scroll
# position. * `{host}`: The host of the current web page. * `{backend}`:
# Either ''webkit'' or ''webengine'' * `{private}` : Indicates when
# private mode is enabled.
# Type: FormatString
c.tabs.title.format = '{current_title}'

# The format to use for the tab title for pinned tabs. The same
# placeholders like for `tabs.title.format` are defined.
# Type: FormatString
c.tabs.title.format_pinned = ''

# The width of the tab bar if it's vertical, in px or as percentage of
# the window.
# Type: PercOrInt
c.tabs.width = '10%'

# Width of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 0

# Whether to wrap when changing tabs.
# Type: Bool
c.tabs.wrap = True

# Whether to start a search when something else than a URL is entered.
# Type: String
# Valid values:
#   - naive: Use simple/naive check.
#   - dns: Use DNS requests (might be slow!).
#   - never: Never search automatically.
c.url.auto_search = 'naive'

# The page to open if :open -t/-b/-w is used without URL. Use
# `about:blank` for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'https://google.com/'

# The URL segments where `:navigate increment/decrement` will search for
# a number.
# Type: FlagList
# Valid values:
#   - host
#   - path
#   - query
#   - anchor
c.url.incdec_segments = ['path', 'query']

# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/?q={}'}

# The page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://google.com'

# The URL parameters to strip with `:yank url`.
# Type: List of String
c.url.yank_ignored_parameters = [
    'ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

# Hide the window decoration when using wayland (requires restart)
# Type: Bool
c.window.hide_decoration = False

# The format to use for the window title. The following placeholders are
# defined:  * `{perc}`: The percentage as a string like `[10%]`. *
# `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
# the current web page * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{id}`: The internal window ID of this window.
# * `{scroll_pos}`: The page scroll position. * `{host}`: The host of
# the current web page. * `{backend}`: Either ''webkit'' or
# ''webengine'' * `{private}` : Indicates when private mode is enabled.
# Type: FormatString
c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'

# The default zoom level.
# Type: Perc
c.zoom.default = '100%'

# The available zoom levels.
# Type: List of Perc
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%',
                 '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

# How much to divide the mouse wheel movements to translate them into
# zoom increments.
# Type: Int
c.zoom.mouse_divider = 512

# Whether the zoom factor on a frame applies only to the text or to all
# content.
# Type: Bool
# c.zoom.text_only = False

config.bind(';', 'set-cmd-text :')

# Bindings for normal mode
# config.bind("P", 'spawn mpv {url}')
# config.bind("P", 'hint links spawn mpv {hint-url}')
# config.bind("<space>", 'spawn --userscript password_fill')
# config.bind("'", 'enter-mode jump_mark')
# config.bind('+', 'zoom-in')
# config.bind('-', 'zoom-out')
# config.bind('.', 'repeat-command')
# config.bind('/', 'set-cmd-text /')
# config.bind(':', 'set-cmd-text :')
# config.bind(';I', 'hint images tab')
# config.bind(';O', 'hint links fill :open -t -r {hint-url}')
# config.bind(';R', 'hint --rapid links window')
# config.bind(';Y', 'hint links yank-primary')
# config.bind(';b', 'hint all tab-bg')
# config.bind(';d', 'hint links download')
# config.bind(';r', 'hint all tab-fg')
# config.bind(';h', 'hint all hover')
# config.bind(';i', 'hint images')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind(';f', 'hint --rapid links tab-bg')
# config.bind(';t', 'hint inputs')
# config.bind(';y', 'hint links yank')
# config.bind('<Alt-1>', 'tab-focus 1')
# config.bind('<Alt-2>', 'tab-focus 2')
# config.bind('<Alt-3>', 'tab-focus 3')
# config.bind('<Alt-4>', 'tab-focus 4')
# config.bind('<Alt-5>', 'tab-focus 5')
# config.bind('<Alt-6>', 'tab-focus 6')
# config.bind('<Alt-7>', 'tab-focus 7')
# config.bind('<Alt-8>', 'tab-focus 8')
# config.bind('<Alt-9>', 'tab-focus -1')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-D>', 'scroll-page 0 -1')
# config.bind('S', 'scroll-page 0 0.5')
# config.bind('<Ctrl-F5>', 'reload -f')
# config.bind('<Ctrl-S>', 'scroll-page 0 1')
# config.bind('<Ctrl-N>', 'open -w')
config.bind('e', 'tab-next')
config.bind('q', 'tab-prev')
config.bind('<Ctrl-Right>', 'tab-next')
config.bind('<Ctrl-Left>', 'tab-prev')
config.bind('<Ctrl-Q>', 'quit')
# config.bind('<Ctrl-Return>', 'follow-selected -t')
# config.bind('<Ctrl-Shift-N>', 'open -p')
# config.bind('<Ctrl-Shift-T>', 'undo')
# config.bind('<Ctrl-Shift-W>', 'close')
# config.bind('<Ctrl-T>', 'open -t')
# config.bind('<Ctrl-Tab>', 'tab-focus last')
# config.bind('d', 'scroll-page 0 -1')
# config.bind('s', 'scroll-page 0 1')
# config.bind('<Ctrl-V>', 'enter-mode passthrough')
# config.bind('<Ctrl-W>', 'tab-close')
# config.bind('<Ctrl-X>', 'navigate decrement')
# config.bind('<Ctrl-^>', 'tab-focus last')
# config.bind('<Ctrl-h>', 'home')
# config.bind('<Ctrl-p>', 'tab-pin')
# config.bind('<Ctrl-s>', 'stop')
# config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
# config.bind('<F11>', 'fullscreen')
# config.bind('m', 'reload')
# config.bind('<Return>', 'follow-selected')
# config.bind('<back>', 'back')
# config.bind('<forward>', 'forward')
# config.bind('=', 'zoom')
# config.bind('?', 'set-cmd-text ?')
# config.bind('@', 'run-macro')
# config.bind('B', 'set-cmd-text -s :quickmark-load -t')
# config.bind('F', 'hint all tab')
# config.bind('G', 'scroll-to-perc')
config.bind('a', 'back')
config.bind('d', 'forward')
# config.bind('M', 'bookmark-add')
# config.bind('N', 'search-prev')
# config.bind('j', 'set-cmd-text -s :open -t ')
# config.bind('PP', 'open -t -- {primary}')
# config.bind('Pp', 'open -t -- {clipboard}')
# config.bind('l', 'tab-focus')
# config.bind('ZQ', 'quit')
# config.bind('ZZ', 'quit --save')
# config.bind('[[', 'navigate prev')
# config.bind(']]', 'navigate next')
# config.bind('`', 'enter-mode set_mark')
# config.bind('ad', 'download-cancel')
# config.bind('b', 'set-cmd-text -s :quickmark-load')
# config.bind('cd', 'download-clear')
config.bind('x', 'tab-close')
# config.bind('f', 'hint')
# config.bind('g$', 'tab-focus -1')
# config.bind('g0', 'tab-focus 1')
# config.bind('gB', 'set-cmd-text -s :bookmark-load -t')
# config.bind('gc', 'tab-clone')
# config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
# config.bind('gU', 'navigate up -t')
# config.bind('g^', 'tab-focus 1')
# config.bind('ga', 'open -t')
# config.bind('gb', 'set-cmd-text -s :bookmark-load')
# config.bind('gd', 'download')
# config.bind('gf', 'view-source')
# config.bind('gg', 'scroll-to-perc 0')
# config.bind('gv', 'tab-move -')
# config.bind('gm', 'tab-move')
# config.bind('go', 'set-cmd-text :open {url:pretty}')
# config.bind('gl', 'tab-move +')
# config.bind('gu', 'navigate up')
# config.bind('t', 'scroll left')
# config.bind('i', 'enter-mode insert')
config.bind('s', 'scroll down')
config.bind('w', 'scroll up')
# config.bind('r', 'scroll right')
# config.bind('M', 'quickmark-save')
# config.bind('n', 'search-next')
# config.bind('J', 'set-cmd-text -s :open ')
# config.bind('pP', 'open -- {primary}')
# config.bind('pp', 'open -- {clipboard}')
# config.bind('gT', 'back -t')
# config.bind('gR', 'forward -t')
config.bind('u', 'undo')
# config.bind('c', 'enter-mode caret')
# config.bind('wB', 'set-cmd-text -s :bookmark-load -w')
# config.bind('wO', 'set-cmd-text :open -w {url:pretty}')
# config.bind('wP', 'open -w -- {primary}')
# config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
# config.bind('wf', 'hint all window')
# config.bind('gw', 'back -w')
# config.bind('wi', 'inspector')
# config.bind('wl', 'forward -w')
# config.bind('wo', 'set-cmd-text -s :open -w')
# config.bind('wp', 'open -w -- {clipboard}')
# config.bind('xO', 'set-cmd-text :open -b -r {url:pretty}')
# config.bind('xb', 'config-cycle statusbar.hide')
# config.bind('xo', 'set-cmd-text -s :open -b')
# config.bind('xt', 'config-cycle tabs.show always switching')
# config.bind('xx', 'config-cycle statusbar.hide ;; config-cycle tabs.show always switching')
# config.bind('yD', 'yank domain -s')
# config.bind('yP', 'yank pretty-url -s')
# config.bind('yT', 'yank title -s')
# config.bind('yY', 'yank -s')
# config.bind('yd', 'yank domain')
# config.bind('yp', 'yank pretty-url')
# config.bind('yt', 'yank title')
# config.bind('yy', 'yank')
# config.bind('{{', 'navigate prev -t')
# config.bind('}}', 'navigate next -t')

# # Bindings for caret mode
# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
# config.bind('<Escape>', 'leave-mode', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'toggle-selection', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('H', 'scroll left', mode='caret')
# config.bind('J', 'scroll down', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('Y', 'yank selection -s', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('c', 'enter-mode normal', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('v', 'toggle-selection', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')

# # Bindings for command mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'command-history-next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'command-history-prev', mode='command')

# # Bindings for hint mode
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'leave-mode', mode='hint')
# config.bind('<Return>', 'follow-hint', mode='hint')

# # Bindings for insert mode
# config.bind('<Ctrl-E>', 'open-editor', mode='insert')
# config.bind('<Escape>', 'leave-mode', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text {primary}', mode='insert')

# # Bindings for passthrough mode
# config.bind('<Ctrl-V>', 'leave-mode', mode='passthrough')

# # Bindings for prompt mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')
# config.bind('n', 'prompt-accept no', mode='prompt')
# config.bind('y', 'prompt-accept yes', mode='prompt')

# # Bindings for register mode
# config.bind('<Escape>', 'leave-mode', mode='register')

# # Zotero Bindings
# config.bind('zz', 'zotero')
# config.bind('zf', 'zotero_link')


# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Gruvbox dark, soft scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

base00 = "#32302f"
base01 = "#3c3836"
base02 = "#504945"
base03 = "#665c54"
base04 = "#bdae93"
base05 = "#d5c4a1"
base06 = "#ebdbb2"
base07 = "#fbf1c7"
base08 = "#fb4934"
base09 = "#fe8019"
base0A = "#fabd2f"
base0B = "#b8bb26"
base0C = "#8ec07c"
base0D = "#83a598"
base0E = "#d3869b"
base0F = "#d65d0e"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base01

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base07

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0F

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base0F

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0F

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base08

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base0B

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base00

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base00

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base00

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base03

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base05

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base00

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base00

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base00

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base02

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base07

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base07

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base05

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base05

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base0E

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base07

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base0F

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base07

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base0F

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = base00
