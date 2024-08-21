# Implement a BandPassFilter class that takes a soundwave (list of frequencies), a lower limit and an upper limit. 
# The class has a method apply() adjusting the frequencies in soundwave such that any frequency 
#   below the lower limit is set to the lower limit, 
#   any frequency above the upper limit is set to the upper limit
#   and frequencies in between are unchanged. 
# The method should return the modified soundwave.

class BandPassFilter:
    def __init__(self, soundwave, lower_limit, upper_limit):
        self.soundwave = soundwave
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def apply(self):
        for i in range(len(self.soundwave)):
            if self.soundwave[i] < self.lower_limit:
                self.soundwave[i] = self.lower_limit
            elif self.soundwave[i] > self.upper_limit:
                self.soundwave[i] = self.upper_limit
        return soundwave

soundwave = [80, 90, 100, 110, 120]
filter    = BandPassFilter(soundwave, 90, 110)

print(filter.apply()) # # => [90, 90, 100, 110, 110]