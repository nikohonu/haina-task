import typing
from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self) -> None:
        self.controller: typing.Any = None

    @abstractmethod
    def setup(self, controller: typing.Any) -> None:
        ...

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def update_task(self, task_id: int, name: str) -> None:
        ...
