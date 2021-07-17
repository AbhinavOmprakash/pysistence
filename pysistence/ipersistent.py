from abc import ABC, abstractmethod


class IPersistent(ABC):
    @abstractmethod
    def cons(self, value):
        pass

    @abstractmethod
    def conj(self, value):
        pass

    @abstractmethod
    def concat(self, value):
        pass
