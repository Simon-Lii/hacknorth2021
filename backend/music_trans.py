import abjad
from audio_transcription.audio_transcript import AudioTranscripter

at = AudioTranscripter('piano.wav')
print(at)

# string = "c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' d''16"
# voice_1 = abjad.Voice(string, name="Voice_1")
# staff_1 = abjad.Staff([voice_1], name="Staff_1")
# pitches = string.split()
# pitches = reversed(pitches)
# retrograde = " ".join(pitches)
# voice_1.extend(retrograde)
# string = string + " " + retrograde
# voice_2 = abjad.Voice(string, name="Voice_2")
# staff_2 = abjad.Staff([voice_2], name="Staff_2")
# clef = abjad.Clef("bass")
# abjad.attach(clef, staff_2[0])
# piano_staff = abjad.StaffGroup(
#     [staff_1, staff_2],
#     lilypond_type="PianoStaff",
#     name="PianoStaff",
# )
# score = abjad.Score([piano_staff], name="Score")
# abjad.show(score)

# save the pdf file to the outer directory
# abjad.show(notes, output_directory=r"..", should_open=False)

# freq_chart = {'16.35': 'C0', '17.32': 'C#0', '18.35': 'D0', '19.45': 'D#0', '20.6': 'E0',
#               '21.83': 'F0', '23.12': 'F#0', '24.5': 'G0', '25.96': 'G#0', '27.5': 'A0',
#               '29.14': 'A#0', '30.87': 'B0', '32.7': 'C1', '34.65': 'C#1', '36.71': 'D1',
#               '38.89': 'D#1', '41.2': 'E1', '43.65': 'F1', '46.25': 'F#1', '49': 'G1',
#               '51.91': 'G#1', '55': 'A1', '58.27': 'A#1', '61.74': 'B1', '65.41': 'C2',
#               '69.3': 'C#2', '73.42': 'D2', '77.78': 'D#2', '82.41': 'E2', '87.31': 'F2',
#               '92.5': 'F#2', '98': 'G2', '103.83': 'G#2', '110': 'A2', '116.54': 'A#2',
#               '123.47': 'B2', '130.81': 'C3', '138.59': 'C#3', '146.83': 'D3', '155.56': 'D#3',
#               '164.81': 'E3', '174.61': 'F3', '185': 'F#3', '196': 'G3', '207.65': 'G#3',
#               '220': 'A3', '233.08': 'A#3', '246.94': 'B3', '261.63': 'C4', '277.18': 'C#4',
#               '293.66': 'D4', '311.13': 'D#4', '329.63': 'E4', '349.23': 'F4', '369.99': 'F#4',
#               '392': 'G4', '415.3': 'G#4', '440': 'A4', '466.16': 'A#4', '493.88': 'B4',
#               '523.25': 'C5', '554.37': 'C#5', '587.33': 'D5', '622.25': 'D#5', '659.26': 'E5',
#               '698.46': 'F5', '739.99': 'F#5', '783.99': 'G5', '830.61': 'G#5', '880': 'A5',
#               '932.33': 'A#5', '987.77': 'B5', '1046.5': 'C6', '1108.73': 'C#6', '1174.66': 'D6',
#               '1244.51': 'D#6', '1318.51': 'E6', '1396.91': 'F6', '1479.98': 'F#6', '1567.98': 'G6',
#               '1661.22': 'G#6', '1760': 'A6', '1864.66': 'A#6', '1975.53': 'B6', '2093': 'C7',
#               '2217.46': 'C#7', '2349.32': 'D7', '2489.02': 'D#7', '2637.02': 'E7', '2793.83':
#                   'F7', '2959.96': 'F#7', '3135.96': 'G7', '3322.44': 'G#7', '3520': 'A7',
#               '3729.31': 'A#7', '3951.07': 'B7', '4186.01': 'C8', '4434.92': 'C#8', '4698.64': 'D8',
#               '4978.03': 'D#8'}


# def build_str(notes):
#     music_str = ''
#     for tup in notes:
#         freq = tup[0]
#         time = tup[1]
#         diff = 500
#         note = ''
#         for key in freq_chart:
#             key_diff = math.abs(int(key) - int(freq))
#             if key_diff < diff:
#                 diff = key_diff
#                 note = freq_chart[key]
#         if diff == 500:
#             return "Frequency out of range."
#         letter = note[:-1]
#         octave = note[-1]
#
#
#     return music_str

# def build_str(notes):
#     music_str = ""
#     for tup in notes:
#         octave_str = ''
#         note = tup[1][:-1].lower()
#         octave = int(tup[1][-1])
#         time = tup[0]
#         if '#' in note:
#             note = note.replace('#', 's')
#         if '♭' in note:
#             note = note.replace('♭', 'f')
#         if octave <= 2:
#             return 'Note out of range.'
#         octave_diff = octave - 3
#         for i in range(octave_diff):
#             octave_str += "'"
#         note_str = note
#         music_str += note_str + octave_str + " "
#
#     return music_str[:-1]
#
# test =
# x = build_str(test)
# print(x)
#
#
# def output_score(music_str, tempo):
#     staff = abjad.Staff(music_str)
#     score = abjad.Score([staff])
#     barline = abjad.deprecated.add_final_bar_line(score)
#     abjad.show(score)
#
#
# output_score(x)

# staff_1 = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
# clef_1 = abjad.Clef("treble")
# abjad.attach(clef_1, staff_1[0])
#
# staff_2 = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
# clef_2 = abjad.Clef("bass")
# abjad.attach(clef_2, staff_2[0])
#
# piano_staff = abjad.StaffGroup(
#     [staff_1, staff_2],
#     lilypond_type="PianoStaff",
#     name="PianoStaff",
# )
# abjad.show(piano_staff)

import math
# string = "c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' d''16"
# voice_1 = abjad.Voice(string, name="Voice_1")
# staff_1 = abjad.Staff([voice_1], name="Staff_1")
# pitches = string.split()
# pitches = reversed(pitches)
# retrograde = " ".join(pitches)
# voice_1.extend(retrograde)
# string = string + " " + retrograde
# voice_2 = abjad.Voice(string, name="Voice_2")
# staff_2 = abjad.Staff([voice_2], name="Staff_2")
# clef = abjad.Clef("bass")
# abjad.attach(clef, staff_2[0])
# piano_staff = abjad.StaffGroup(
#     [staff_1, staff_2],
#     lilypond_type="PianoStaff",
#     name="PianoStaff",
# )
# score = abjad.Score([piano_staff], name="Score")
# abjad.show(score)

# save the pdf file to the outer directory
# abjad.show(notes, output_directory=r"..", should_open=False)

freq_chart = {'16.35': 'C0', '17.32': 'C#0', '18.35': 'D0', '19.45': 'D#0', '20.6': 'E0',
              '21.83': 'F0', '23.12': 'F#0', '24.5': 'G0', '25.96': 'G#0', '27.5': 'A0',
              '29.14': 'A#0', '30.87': 'B0', '32.7': 'C1', '34.65': 'C#1', '36.71': 'D1',
              '38.89': 'D#1', '41.2': 'E1', '43.65': 'F1', '46.25': 'F#1', '49': 'G1',
              '51.91': 'G#1', '55': 'A1', '58.27': 'A#1', '61.74': 'B1', '65.41': 'C2',
              '69.3': 'C#2', '73.42': 'D2', '77.78': 'D#2', '82.41': 'E2', '87.31': 'F2',
              '92.5': 'F#2', '98': 'G2', '103.83': 'G#2', '110': 'A2', '116.54': 'A#2',
              '123.47': 'B2', '130.81': 'C3', '138.59': 'C#3', '146.83': 'D3', '155.56': 'D#3',
              '164.81': 'E3', '174.61': 'F3', '185': 'F#3', '196': 'G3', '207.65': 'G#3',
              '220': 'A3', '233.08': 'A#3', '246.94': 'B3', '261.63': 'C4', '277.18': 'C#4',
              '293.66': 'D4', '311.13': 'D#4', '329.63': 'E4', '349.23': 'F4', '369.99': 'F#4',
              '392': 'G4', '415.3': 'G#4', '440': 'A4', '466.16': 'A#4', '493.88': 'B4',
              '523.25': 'C5', '554.37': 'C#5', '587.33': 'D5', '622.25': 'D#5', '659.26': 'E5',
              '698.46': 'F5', '739.99': 'F#5', '783.99': 'G5', '830.61': 'G#5', '880': 'A5',
              '932.33': 'A#5', '987.77': 'B5', '1046.5': 'C6', '1108.73': 'C#6', '1174.66': 'D6',
              '1244.51': 'D#6', '1318.51': 'E6', '1396.91': 'F6', '1479.98': 'F#6', '1567.98': 'G6',
              '1661.22': 'G#6', '1760': 'A6', '1864.66': 'A#6', '1975.53': 'B6', '2093': 'C7',
              '2217.46': 'C#7', '2349.32': 'D7', '2489.02': 'D#7', '2637.02': 'E7', '2793.83':
                  'F7', '2959.96': 'F#7', '3135.96': 'G7', '3322.44': 'G#7', '3520': 'A7',
              '3729.31': 'A#7', '3951.07': 'B7', '4186.01': 'C8', '4434.92': 'C#8', '4698.64': 'D8',
              '4978.03': 'D#8'}


# def build_str(notes):
#     music_str = ''
#     for tup in notes:
#         freq = tup[0]
#         time = tup[1]
#         diff = 500
#         note = ''
#         for key in freq_chart:
#             key_diff = math.abs(int(key) - int(freq))
#             if key_diff < diff:
#                 diff = key_diff
#                 note = freq_chart[key]
#         if diff == 500:
#             return "Frequency out of range."
#         letter = note[:-1]
#         octave = note[-1]
#
#
#     return music_str

def build_str(ori_notes):
    tempo = ori_notes[1]
    quarter = 1/(tempo/60)
    range_of_notes = [quarter/4, quarter/2, quarter, quarter*2, quarter*4]
    notes = ori_notes[2]
    music_str = ""
    for i in range(len(notes)):
        octave_str = ''
        note = notes[i][1][:-1].lower()
        octave = int(notes[i][1][-1])
        time = notes[i][0]
        time_str = ''
        if i == len(notes):
            num_notes = len(notes) - 1
            num = num_notes % 4
            if num == 0:
                time_str = '1'
            elif num == 1:
                time_str = '2.'
            elif num == 2:
                time_str = '2'
            else:
                time_str = '4'
        else:
            next_note_time = notes[i+1][0]
            duration = next_note_time - time
            duration_diff = abs(range_of_notes[0] - duration)
            time_str = '16'
            for j in range(1, len(range_of_notes)):
                if abs(range_of_notes[j] - duration) < duration_diff:
                    duration_diff = abs(range_of_notes[j] - duration)
                    note_length = 2**(abs(4-i))
                    time_str = str(note_length)
        if '#' in note:
            note = note.replace('#', 's')
        if '♭' in note:
            note = note.replace('♭', 'f')
        if octave <= 2:
            return 'Note out of range.'
        octave_diff = octave - 3
        for k in range(octave_diff):
            octave_str += "'"
        note_str = note
        music_str += note_str + octave_str + time_str + " "

    return music_str[:-1]


def output_score(music_str, tempo):
    staff = abjad.Staff(music_str)
    score = abjad.Score([staff])
    barline = abjad.deprecated.add_final_bar_line(score)
    abjad.show(score)


# staff_1 = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
# clef_1 = abjad.Clef("treble")
# abjad.attach(clef_1, staff_1[0])
#
# staff_2 = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
# clef_2 = abjad.Clef("bass")
# abjad.attach(clef_2, staff_2[0])
#
# piano_staff = abjad.StaffGroup(
#     [staff_1, staff_2],
#     lilypond_type="PianoStaff",
#     name="PianoStaff",
# )
# abjad.show(piano_staff)
