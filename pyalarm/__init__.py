#!/usr/bin/env python

# bird sound from http://www.freesound.org/people/klankbeeld/

from .clock import Clock, Alarm, Song


def test():
    print 'T'


if __name__ == '__main__':
    a1 = Alarm('22:21', test, Song('bird.ogg'))
    a2 = Alarm('07:15', test)

    # ClockApp(
    #     Song('bird.ogg'),
    #     Clock([a1, a2])
    # ).run()

    Clock([a1, a2]).start()
