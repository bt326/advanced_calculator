from app.calculation import Calculation


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)

    assert calc.operation == "add"
    assert calc.operand1 == 2
    assert calc.operand2 == 3
    assert calc.result == 5
    assert calc.timestamp is not None


def test_calculation_to_dict():
    calc = Calculation("add", 2, 3, 5)
    data = calc.to_dict()

    assert data["operation"] == "add"
    assert data["operand1"] == 2
    assert data["operand2"] == 3
    assert data["result"] == 5
    assert "timestamp" in data

def test_calculation_to_dict_full():
    calc = Calculation("add", 2, 3, 5)
    data = calc.to_dict()

    assert data["operation"] == "add"
    assert data["operand1"] == 2
    assert data["operand2"] == 3
    assert data["result"] == 5
    assert "timestamp" in data


def test_calculation_str_format():
    calc = Calculation("add", 2, 3, 5)
    text = str(calc)

    assert "ADD" in text
    assert "5" in text