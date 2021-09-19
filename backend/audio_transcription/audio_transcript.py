import aubio
import numpy as np
import subprocess
import os

class AudioTranscripter:
    def __init__(self, filename):
        path_file = os.path.dirname(os.path.realpath(__file__))
        aubio_pitch = subprocess.getoutput(f'aubio pitch "{path_file}/temp_song/{str(filename)}"').split()
        aubio_beat = subprocess.getoutput(f'aubio onset "{path_file}/temp_song/{str(filename)}"').split()
        print(aubio_beat)
        self.filename = filename
        self.pitch = {}
        self.beat = {}
        self.tempo = subprocess.getoutput(f'aubio tempo "{path_file}/temp_song/{str(filename)}"').split()[0]
        self.fastest_note = (float(self.tempo) / 60) / 16
        i = 0
        print(aubio_pitch)
        while i < len(aubio_pitch):
            timestamp = "{:.2f}".format(float(aubio_pitch[i]))
            freq = float(aubio_pitch[i + 1])
            if freq > 0:
                if not timestamp in self.pitch:
                    self.pitch[timestamp] = freq
            i += 2
        i = 0
        temp_beat = []
        while i < len(aubio_beat):
            timestamp = "{:.2f}".format(float(aubio_beat[i]))
            if not timestamp in self.beat:
                if i > 0:
                    if float(timestamp) - float(temp_beat[-1]) > self.fastest_note:
                        temp_beat.append(timestamp)
                        self.beat[timestamp] = 1
                else:
                    temp_beat.append(timestamp)
                    self.beat[timestamp] = 1
            i += 1

    def convert(self):
        musical_score = []
        for timestamp in self.beat:
            if timestamp in self.pitch:
                freq = self.pitch[timestamp]
                letter_note = aubio.freq2note(freq)
                musical_score.append((timestamp, letter_note))
        return (self.filename, self.tempo, musical_score)
