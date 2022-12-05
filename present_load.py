class Sleigh:
    def __init__(self):
        self.list_of_presents = []

    def add_present(self, present: str):
        self.list_of_presents.append(present)


class Elf:
    def __init__(self):
        self.carried_present = None

    def pack_into(self, sleigh: Sleigh):
        sleigh.add_present(self.carried_present)
        self.carried_present = None


class ToyMachine:
    def __init__(self):
        self.present_made = None

    def make_present(self, present: str) -> str:
        return present

    def give_present(self, elf: Elf):
        elf.carried_present = self.present_made
