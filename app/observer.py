from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Base observer class.
    """

    @abstractmethod
    def update(self, calculation):
        pass