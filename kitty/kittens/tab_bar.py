# pyright: reportMissingImports=false
import datetime

import dbus

from kitty.boss import get_boss
from kitty.fast_data_types import Screen, add_timer
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    Formatter,
    TabBarData,
    as_rgb,
    draw_attributed_string,
    draw_tab_with_powerline,
)

timer_id = None
screen_width = None


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    global timer_id
    global screen_width
    screen_width = screen.columns
    max_title_length = 30

    if timer_id is None:
        timer_id = add_timer(_redraw_tab_bar, 2.0, True)
    draw_tab_with_powerline(
        draw_data,
        screen,
        tab,
        before,
        max_title_length,
        index,
        is_last,
        extra_data,
    )
    if is_last:
        draw_right_status(draw_data, screen)
    return screen.cursor.x


def draw_right_status(draw_data: DrawData, screen: Screen) -> None:
    # The tabs may have left some formats enabled. Disable them now.
    draw_attributed_string(Formatter.reset, screen)
    cells = create_cells()
    # Drop cells that wont fit
    while True:
        if not cells:
            return
        padding = screen.columns - screen.cursor.x - sum(len(c) + 3 for c in cells)
        if padding >= 0:
            break
        cells = cells[1:]

    if padding:
        screen.draw(" " * padding)

    tab_bg = as_rgb(int(draw_data.inactive_bg))
    tab_fg = as_rgb(int(draw_data.inactive_fg))
    default_bg = as_rgb(int(draw_data.default_bg))
    for cell in cells:
        # Draw the separator
        if cell == cells[0]:
            screen.cursor.fg = tab_bg
            screen.draw("")
        else:
            screen.cursor.fg = default_bg
            screen.cursor.bg = tab_bg
            screen.draw("")
        screen.cursor.fg = tab_fg
        screen.cursor.bg = tab_bg
        screen.draw(f" {cell} ")


def create_cells() -> list[str]:
    now = datetime.datetime.now()
    return [
        # currently_playing(),
        now.strftime("%a %-d %b"),
        now.strftime("%H:%M:%S"),
    ]


def currently_playing():
    bus = dbus.SessionBus()
    for service in bus.list_names():
        if service.startswith("org.mpris.MediaPlayer2."):
            player = dbus.SessionBus().get_object(service, "/org/mpris/MediaPlayer2")
            status = player.Get(
                "org.mpris.MediaPlayer2.Player",
                "PlaybackStatus",
                dbus_interface="org.freedesktop.DBus.Properties",
            )

            metadata = player.Get(
                "org.mpris.MediaPlayer2.Player",
                "Metadata",
                dbus_interface="org.freedesktop.DBus.Properties",
            )

            for key, value in metadata.items():
                if key == "xesam:title" and status == "Playing":
                    width = int(screen_width * 0.3)
                    return f"  {value[:width]}"

    return " "


def _redraw_tab_bar(timer_id):
    for tm in get_boss().all_tab_managers:
        tm.mark_tab_bar_dirty()
