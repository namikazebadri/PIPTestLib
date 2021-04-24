from pylib.commons import Mannerism


def test_mannerism():
    name = "Avicenna"

    mannerism = Mannerism("Avicenna")

    expected_manner = f"Hi {name}, how are you today?"

    assert mannerism.create() == expected_manner
