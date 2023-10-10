from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Sequence, Callable, Any, Iterable, Generator

T = TypeVar('T')


class List(metaclass=ABCMeta, Generic[T]):
    @abstractmethod
    def remove(self, item: T):
        pass

    @abstractmethod
    def pop(self, index=None) -> T:
        pass

    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def extend(self, iterable: Sequence[T]) -> None:
        pass

    @abstractmethod
    def sort(self, key: Callable[[T], Any], reverse: bool = False):  # TODO ANY Protocol
        pass

    @abstractmethod
    def insert(self, item: T, position: int):
        pass

    @abstractmethod
    def __iter__(self) -> Iterable[T]:
        pass

    @abstractmethod
    def __next__(self) -> Generator[T, Any, Any]:
        pass

    @abstractmethod
    def __getitem__(self, item) -> T:
        pass

    @abstractmethod
    def __setitem__(self, key: int, value: T):
        pass

    @abstractmethod
    def __setslice__(self, i, j, sequence):  # TODO
        pass

    @abstractmethod
    def __delslice__(self, i, j):  # TODO
        pass
