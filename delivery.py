class ToyMachine:
    def __init__(self):
        self.present_made = None

    def make_present(self, present):
        return present

    def give_present(self, elf):
        elf.carried_present = self.present_made


class Elf:
    def __init__(self):
        self.carried_present = None

    def pack_into(self, sleigh):
        sleigh.list_of_presents.append(self.carried_present)
        self.carried_present = None


class Sleigh:
    def __init__(self):
        self.list_of_presents = []
