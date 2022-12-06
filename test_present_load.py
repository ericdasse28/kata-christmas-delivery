import pytest

from present_load import Elf, Sleigh, ToyMachine, present_loading_process


@pytest.mark.parametrize(
    "present_to_make",
    ["Joystick", "Spider Man Game", "Detective Game", "Samsung Galaxy S23"],
)
def test_toy_machine_can_make_a_present(present_to_make):
    toy_machine = ToyMachine()

    toy_machine.make_present(present_to_make)

    assert toy_machine.last_present_made == present_to_make


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
    toy_machine.last_present_made = present_made
    elf = Elf()

    toy_machine.give_present_to(elf)

    assert elf.carried_present == toy_machine.last_present_made


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
def test_elf_can_pack_present_onto_santa_sleigh(present_to_pack):
    elf = Elf()
    elf.carried_present = present_to_pack
    sleigh = Sleigh()
    initial_length = len(sleigh.list_of_presents)

    elf.pack_onto(sleigh)

    assert elf.carried_present is None
    assert len(sleigh.list_of_presents) == initial_length + 1
    assert present_to_pack in sleigh.list_of_presents


@pytest.mark.parametrize(
    "santa_list",
    [
        (["Gameboy", "World Peace", "Jingle bells"]),
        (["Gameboy", "World Peace", "Jingle bells", "Snowman"]),
        (["Playstation 5", "iPhone 14 plus", "Jingle bells", "Curry8"]),
        (
            [
                "Batarang",
                "Chinese food",
                "Socks",
                "Attack on titan volumes",
                "Detective Conan mangas",
                "Theater tickets",
            ]
        ),
    ],
)
def test_present_loading_process(santa_list):
    toy_machine = ToyMachine()
    elf = Elf()
    sleigh = Sleigh()

    present_loading_process(
        toy_machine=toy_machine, elf=elf, sleigh=sleigh, santa_list=santa_list
    )

    assert toy_machine.last_present_made == santa_list[-1]
    assert elf.carried_present is None
    for present_to_offer in santa_list:
        assert present_to_offer in sleigh.list_of_presents
