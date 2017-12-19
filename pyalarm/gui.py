
# -*- coding: utf-8 -*-

import Tkinter as tk
import time


class ClockGui(object):
    def __init__(self, fullscreen=True):
        self.is_fullscreen = fullscreen
        self.background_color = 'black'
        self.text_color = 'green'
        self.time_format = '%H:%M:%S'
        self.blink_color_a = [30, 30, 30]
        self.blink_color_b = [242, 216, 65]

        self.root = tk.Tk()
        self.blink_frame = tk.Frame()
        self.time_label = tk.Label()

        self._build()

    def _build(self):
        self.root.title('Clock')
        self.root.configure(background=self.background_color, cursor='none')

        self.root.bind("<F11>", self._toggle_fullscreen)
        self.root.bind("<Escape>", self.close)

        self._build_time_label()

        self._toggle_fullscreen()

    def _build_time_label(self):
        self.time_label.destroy()
        self.time_label = TimeLabel(self.root, self.background_color, self.text_color, self.time_format)

    def _build_blink_frame(self):
        self.blink_frame.destroy()
        self.blink_frame = BlinkFrame(self.root, self.blink_color_a, self.blink_color_b)

    def _toggle_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", self.is_fullscreen)
        self.is_fullscreen = not self.is_fullscreen

    def alarmflash(self, event=None, stop_callback=None):
        print 'ClockGui.alarmflash():', stop_callback

        self.time_label.destroy()

        self.root.bind('<Button-1>', lambda e, cb=stop_callback: self.snooze(e, cb))

        self.root.after(10000, self._build_blink_frame)

    def snooze(self, event=None, stop_callback=None):
        print 'ClockGui.snooze1() event:', event
        print 'ClockGui.snooze1():', stop_callback

        self.blink_frame.destroy()
        self._build_time_label()

        if stop_callback:
            print 'snooze2():', stop_callback
            stop_callback.run()

    def run(self):
        self.root.mainloop()

    def close(self, event=None):
        self.root.destroy()
        self.root.quit()


# -------------------------------------------------------------------


class TimeLabel(tk.Label):
    def __init__(self, root, bg, fg, time_format):
        tk.Label.__init__(
            self,
            root,
            text='clock',
            font=('Comic Sans MS', 50),
            background=bg,
            foreground=fg
        )

        self.pack(expand=True, anchor='c')

        self.time_format = time_format

        self.ticking = True
        self._tick()

    def _tick(self):
        if not self.ticking:
            return

        now = time.strftime(self.time_format)
        self.configure(text=now)

        self.after(1000, self._tick)


# -------------------------------------------------------------------


class BlinkFrame(tk.Frame):
    def __init__(self, root, color_a, color_b):
        tk.Frame.__init__(
            self,
            root
        )
        self.configure(background='red')
        self.pack(expand=True, anchor='c', fill='both')

        self.color_a = color_a
        self.color_b = color_b

        self._blinking = True
        self._blink()

    def _blink(self, state=None, step=1):
        if not self._blinking:
            return

        if state is None:
            state = self.color_a

        # advance color but within limits
        state = map(lambda x, a, b: x+step if a <= x+step <= b else x, state, self.color_a, self.color_b)

        # change direction if limit reached
        if state == self.color_a:
            step = 1
        elif state == self.color_b:
            step = -1

        hexcolor = '#' + ('{:02x}'*3).format(*state)

        self.configure(background=hexcolor)

        self.after(50, self._blink, state, step)


# -------------------------------------------------------------------
