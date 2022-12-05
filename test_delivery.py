import pytest

from delivery import Elf, Sleigh, ToyMachine


@pytest.mark.parametrize(
    "present_to_make",
    ["Joystick", "Spider Man Game", "Detective Game", "Samsung Galaxy S23"],
)
def test_toy_machine_can_make_a_present(present_to_make):
    toy_machine = ToyMachine()

    present_made = toy_machine.make_present(present_to_make)

    assert present_made == present_to_make


@pytest.mark.parametrize(
    "present_made",
    [
        "Fullmetal album",
        "Air Jordan shoes",
        "Curry 8",
        "Dragon Ball Xenoverse",
        "Friends expo",
    ],
)
def test_toy_machine_can_give_a_present_to_elf(present_made):
    toy_machine = ToyMachine()
    toy_machine.present_made = present_made
    elf = Elf()

    toy_machine.give_present(elf)

    assert elf.carried_present == toy_machine.present_made


@pytest.mark.parametrize(
    "present_to_pack",
    [
        "Fullmetal album",
        "Air Jordan shoes",
        "Curry 8",
        "Dragon Ball Xenoverse",
        "Friends expo",
    ],
)
def test_elf_can_pack_present_into_santa_sleigh(present_to_pack):
    elf = Elf()
    elf.carried_present = present_to_pack
    sleigh = Sleigh()
    initial_length = len(sleigh.list_of_presents)

    elf.pack_into(sleigh)

    assert elf.carried_present is None
    assert len(sleigh.list_of_presents) == initial_length + 1
    assert present_to_pack in sleigh.list_of_presents
