#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .clock import Clock, Alarm, Song
from .gui import ClockGui
from .callback import Callback

import os


def test():
    print 'T'


def run():
    path = os.path.dirname(os.path.realpath(__file__))

    g = ClockGui(fullscreen=False)

    from datetime import datetime, timedelta
    now = datetime.now()
    now += timedelta(minutes=1)
    nowstr = now.strftime('%H:%M')
    print nowstr

    a1 = Alarm(alarm_time=nowstr, alarm_song=Song(path + '/bird.ogg'))
    a1.alarm_callback = Callback(g.alarmflash, [None, Callback(a1.stop)])
    print 'main.run():', a1, a1.stop
    print 'main.a1.cb:', a1.alarm_callback

    a2 = Alarm('07:15', Callback(test))

    c = Clock([a1, a2])
    c.start()

    # run gui, waits until gui is quited
    g.run()

    c.stop()


if __name__ == '__main__':
    run()
