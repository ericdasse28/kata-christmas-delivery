import pytest

from delivery import ToyMachine


@pytest.mark.parametrize(
    "present_to_make",
    ["Joystick", "Spider Man Game", "Detective Game", "Samsung Galaxy S23"],
)
def test_toy_machine_can_make_a_present(present_to_make):
    toy_machine = ToyMachine()

    present_made = toy_machine.make_present(present_to_make)

    assert present_made == present_to_make
