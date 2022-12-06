class Sleigh:
    # TODO: add a method has_present
    def __init__(self):
        self.list_of_presents = []

    def add_present(self, present: str):
        self.list_of_presents.append(present)


class Elf:
    def __init__(self):
        self.carried_present = None

    def pack_onto(self, sleigh: Sleigh):
        sleigh.add_present(self.carried_present)
        self.carried_present = None


class ToyMachine:
    def __init__(self):
        self.last_present_made = None

    def make_present(self, present: str) -> str:
        self.last_present_made = present

    def give_present_to(self, elf: Elf):
        elf.carried_present = self.last_present_made


def present_loading_process(
    toy_machine: ToyMachine, elf: Elf, sleigh: Sleigh, santa_list: list
):
    for present in santa_list:
        toy_machine.make_present(present)
        toy_machine.give_present_to(elf)

        elf.pack_onto(sleigh)
