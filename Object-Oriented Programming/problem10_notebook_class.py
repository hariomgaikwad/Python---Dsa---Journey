# Exercise 10: Notebook class

# Logic
# __init__() creates an empty list notes.
# add_note() adds a new note using append().
# show_notes() displays all notes with numbering.
# enumerate(..., start=1) is used to print note numbers starting from 1.

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")


notebook = Notebook()

notebook.add_note("Buy groceries")
notebook.add_note("Read a book")
notebook.add_note("Call the doctor")

notebook.show_notes()