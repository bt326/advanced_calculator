class CalculatorMemento:
    """
    Stores snapshot of calculation history.
    """

    def __init__(self, state):
        self._state = list(state)

    def get_state(self):
        return list(self._state)