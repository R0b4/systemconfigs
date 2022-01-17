####################################
# QTILE CONFIG BY MAARTEN BRUYNINX #
####################################

# Imports
from typing import List, Text  # noqa: F401
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook
import os
import subprocess

from colors.blackqtile import *

# Some quick settings
mod = "mod4"
terminal = "alacritty"
browser = "brave"
def_font = "Hack Nerd Font"

home_dir = os.path.expanduser("~")

@hook.subscribe.startup_once
def autostart():
    os.system("sh ~/.config/qtile/startup.sh")
    return
    
# Keybinds
keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.shrink_main(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_main(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.shrink(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    Key([mod], 'b', lazy.spawn('firefox')),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "s", lazy.spawn("rofi -modi drun -show")),
    Key([mod], "p", lazy.spawn("rofi -modi \"power:~/.config/rofi/scripts/power\" -show power")),
    Key([mod], "i", lazy.spawn("sh " + home_dir + "/.config/rofi/scripts/rofi-wifi-menu.sh")),
    Key([mod], "v", lazy.spawn(terminal + "-e alsamixer")),

    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),

    Key([], "F9", lazy.spawn("amixer -q sset Master 5%- unmute")),
    Key([], "F10", lazy.spawn("amixer -q sset Master 5%+ unmute")),
    Key([], "F8", lazy.spawn("amixer -q sset Master toggle"))
]

# Groups
# I have 9 groups declared, but will autohide the ones not in use
group_names = [
    ("1", {'layout': 'Columns'}),
    ("2", {'layout': 'Columns'},),
    ("3", {'layout': 'Columns'}),
    ("4", {'layout': 'Columns'}),
    ("5", {'layout': 'Columns'}),
    ("6", {'layout': 'Columns'}),
    ("7", {'layout': 'Columns'}),
    ("8", {'layout': 'Columns'}),
    ("9", {'layout': 'Columns'})
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group 

# Layout theme defines how to place windows in my layout (I only use one layout)
layout_theme = {
    "border_width": 1,
    "margin": 8,
    "border_focus": b,
    "border_normal": background_dark,
}
layouts = [
    layout.MonadTall(**layout_theme),
]

widget_defaults = dict(
    font=def_font,
    fontsize = 16,
    padding = 7,
    background= background_dark,
    foreground = foreground
)
extension_defaults = widget_defaults.copy()

# Incase we need spacing
dark_sep = widget.Sep(linewidth = 0, padding = 6, background = background_dark, foreground = background_dark)
light_sep = widget.Sep(linewidth = 0, padding = 6, background = background_light, foreground = background_light)

# List of widgets, to display on the bottom bar
widgets = [
    #arch icon
    dark_sep,
    widget.Image(filename = "~/.config/qtile/img/arch.png",scale = "Trye", mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}),
    dark_sep,
    
    # Group box
    dark_sep,
    widget.GroupBox(
        margin_y = 3,
        margin_x = 0,
        padding_y = 5,
        padding_x = 3,
        borderwidth = 3,
        disable_drag = True,
        block_highlight_text_color = foreground,
        active = foregroundvague,
        rounded = False,
        highlight_color = background_dark,
        highlight_method = "line",
        hide_unused = True,
        this_current_screen_border = foreground,
        this_screen_border = foreground,
        spacing = 20, fontsize = 16,
        font=def_font
    ),
    dark_sep,
    widget.TextBox(text = '\ue0b0', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),

    light_sep,
    widget.WindowName(background = background_light, font=def_font),
    light_sep,

    widget.TextBox(text = '\ue0b2', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),
    dark_sep,
    
    widget.Battery(battery=0, format=" {percent:2.0%}", background=background_dark, foreground=green, update_interval=0.3),
    widget.TextBox(text=" 奄", foreground=blue),
    widget.Volume(foreground=blue, volume_up_command="p"),
    dark_sep, dark_sep,
    # CPU
    widget.CPU(foreground = yellow, format = '  CPU{load_percent: 5.1f}%'
            ,mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
    ),
    widget.Memory(foreground = yellow, measure_mem= 'G', format='   MEM{MemUsed: 5.1f}{mm} ', 
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
    ),
    # Clock
    widget.Clock(foreground = purple, format = "   %a %b %d    %H:%M "),
    widget.TextBox(
        text="  ",
        countdown_start=1,
        foreground=red,
        font = def_font,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e reboot')}
    ),
    widget.TextBox(
        text="  ",
        countdown_start=1,
        foreground=red,
        font = def_font,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e shutdown now')}
    ),
    dark_sep,
    dark_sep,
]

# need to re-create the group box or it won't work on 2 monitors
group_and_middle = [
        # Group box   
        dark_sep,
        widget.GroupBox(
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            disable_drag = True,
            block_highlight_text_color = foreground,
            active = foregroundvague,
            rounded = False,
            highlight_color = background_dark,
            highlight_method = "line",
            hide_unused = True,
            this_current_screen_border = foreground,
            this_screen_border = foreground,
            spacing = 20, fontsize = 25
        ),
        widget.TextBox(text = '\ue0b0', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),
        # Middle side
        # Current window
        light_sep,
        widget.WindowName(background = background_light),
        light_sep,
        # Systemtray
        widget.Systray(background = background_light),
        light_sep,
]

# Append the bar to the bottom of the screen

screens = [
    Screen(
        bottom=bar.Bar(widgets,50, background="#00000000")
    ),
    Screen(
        bottom=bar.Bar(widgets[:4] + group_and_middle + widgets[11:],50)),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, 'shift'], "Button1", lazy.window.disable_floating()),
    Click([mod], "Button1", lazy.window.bring_to_front()) 
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"
