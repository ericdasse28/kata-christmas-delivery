import pytest

from delivery import Elf, ToyMachine


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

    assert elf.current_present == toy_machine.present_made
