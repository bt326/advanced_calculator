from app.observer import Observer


def test_observer_update_method():
    """
    Ensure Observer abstract class can be subclassed
    and update method works as expected.
    """

    class DummyObserver(Observer):
        def update(self, calculation):
            return "updated"

    dummy = DummyObserver()
    result = dummy.update(None)

    assert result == "updated"