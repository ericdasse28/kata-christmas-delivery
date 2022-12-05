class ToyMachine:
    def __init__(self):
        self.present_made = None

    def make_present(self, present):
        return present

    def give_present(self, elf):
        elf.current_present = self.present_made


class Elf:
    def __init__(self):
        self.current_present = None  # TODO: rename to carried_present

    def pack_into(self, sleigh):
        sleigh.list_of_presents.append(self.current_present)
        self.current_present = None


class Sleigh:
    def __init__(self):
        self.list_of_presents = []
