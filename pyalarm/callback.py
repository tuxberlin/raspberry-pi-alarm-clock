
# -*- coding: utf-8 -*-


class Callback(object):
    def __init__(self, callback, parameters={}):
        self.callback = callback
        self.parameters = parameters

    def run(self):
        self.callback(**self.parameters)

    def __repr__(self):
        return '<{}({}, {})>'.format(self.__class__.__name__, self.callback, self.parameters)
