class ToyMachine:
    def __init__(self):
        self.present_made = None

    def make_present(self, present):
        return present

    def give_present(self, elf):
        elf.current_present = self.present_made


class Elf:
    def __init__(self):
        self.current_present = "present"
