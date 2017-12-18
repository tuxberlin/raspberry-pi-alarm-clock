
# -*- coding: utf-8 -*-

from datetime import datetime
from pygame import mixer
from threading import Timer


# -------------------------------------------------------------------


class Clock(object):
    def __init__(self, alarms):
        self.alarms = alarms
        self._ticking = False
        self.time = None

    def _tick(self):
        if not self._ticking:
            return

        self.time = datetime.now().replace(year=1900, month=1, day=1, microsecond=0)

        for alarm in self.alarms:
            diff = abs((alarm.time - self.time).total_seconds())

            if diff <= 1:
                alarm.start()

        Timer(1, self._tick).start()

    def start(self):
        self._ticking = True
        self._tick()

    def stop(self):
        self._ticking = False

        for alarm in self.alarms:
            alarm.stop()


# -------------------------------------------------------------------


class Alarm(object):
    def __init__(self, alarm_time, alarm_callback=None, alarm_song=None, time_format='%H:%M'):
        self.alarm_time = alarm_time
        self.alarm_callback = alarm_callback
        self.alarm_song = alarm_song

        self.time = datetime.strptime(alarm_time, time_format)
        self._enabled = True
        self._ringing = False

    def start(self):
        if self._ringing or not self._enabled:
            return

        self._ringing = True

        if self.alarm_song:
            self.alarm_song.start()

        if self.alarm_callback:
            self.alarm_callback.run()

    def stop(self):
        self._ringing = False

        if self.alarm_song:
            self.alarm_song.stop()


# -------------------------------------------------------------------


class Song(object):
    def __init__(self, filepath, fadein=0, volume=1.0):
        self.fadein = fadein
        self.volume = volume

        # test if file exists
        open(filepath).close()

        mixer.init()
        self.sound = mixer.Sound(filepath)

    def start(self):
        self.sound.set_volume(self.volume)
        self.sound.play(-1, fade_ms=self.fadein)

    def stop(self):
        self.sound.stop()


# -------------------------------------------------------------------
