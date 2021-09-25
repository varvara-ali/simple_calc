class Note:
    def __init__(self, note, is_long=False):
        N = 7
        self.PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
        self.INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
        self.long_notes = {"до": 'до-о', "ре": 'ре-э', "ми": 'ми-и', "фа": 'фа-а',
                           "соль": 'со-оль', "ля": 'ля-а', "си": 'си-и'}
        if is_long:
            self.note = self.LONG_PITCHES[note]
            self.pitches = self.LONG_PITCHES
        else:
            self.note = note
            self.pitches = self.PITCHES

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note

    def __eq__(self, other):
        return self.note == other.note

    def __lt__(self, other):
        return self.pitches.index(self.note) < self.pitches.index(other.note)

    def __le__(self, other):
        return self == other or self < other

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self == other or self < other

    def __lshift__(self, step):
        self.note = self.pitches[self.pitches.index(self.note) - step % len(self.pitches)]
        return self.note

    def __rshift__(self, step):
        shift = step % len(self.pitches)
        if shift > len(self.pitches):
            shift -= len(self.pitches)
        self.note = self.pitches[self.pitches.index(self.note) + shift] % len(self.pitches)
        return self.note


def get_interval(note1: Note, note2: Note):
    PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
    LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
    INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
    return abs(PITCHES.index(note1.note) - PITCHES.index(note2.note))


class LoudNote:
    def __init__(self, note):
        self.notes = {"до": 'ДО', "ре": 'РЕ', "ми": 'МИ', "фа": 'ФА',
                      "соль": 'СОЛЬ', "ля": 'ЛЯ', "си": 'СИ'}

        self.note = self.notes[note]

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note



class NoteWithOctave:
    PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
