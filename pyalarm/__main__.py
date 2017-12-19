#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .clock import Clock, Alarm, Song
from .gui import ClockGui
from .callback import Callback

import os


def run():
    path = os.path.dirname(os.path.realpath(__file__))

    # from datetime import datetime, timedelta
    # now = datetime.now()
    # now += timedelta(minutes=1)
    # nowstr = now.strftime('%H:%M')
    # nowstr2 = (now + timedelta(minutes=1)).strftime('%H:%M')
    # print nowstr
    # print nowstr2

    alarm1 = '08:10'

    g = ClockGui(fullscreen=True)

    a1 = Alarm(alarm_time=alarm1, alarm_song=Song(path + '/bird.ogg'))
    a1.alarm_callback = Callback(g.start_flashing, {'stop_callback': Callback(a1.stop)})

    c = Clock([a1])
    c.start()

    # run gui, waits until gui is quited
    g.run()

    c.stop()


if __name__ == '__main__':
    run()
