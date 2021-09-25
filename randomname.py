class Note:
    def __init__(self, note):
        self.note = note

    def play(self):
        print(self.note)

do = Note("до")
sol = Note("соль")
sol.play()
do.play()