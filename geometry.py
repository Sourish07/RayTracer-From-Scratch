from abc import ABC, abstractmethod


class Geometry(ABC):
    @abstractmethod
    def hit(self, r):
        raise NotImplementedError()

    @abstractmethod
    def normal_at(self, pos):
        raise NotImplementedError()
