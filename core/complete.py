import readline
from core.array import array

class auto(object):
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

def complete(array):
    completer = auto(array)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab:complete')
