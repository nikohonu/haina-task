import typing
from datetime import datetime

from haina_task.models.model import Model
from haina_task.views.typer_view import TyperView


class Controller:
    def __init__(self, model: Model, view: TyperView) -> None:
        self.model = model
        self.view = view

    def start(self) -> None:
        self.view.setup(self)
        self.view.start()

    def add_task(self, task) -> None:
        task_id = self.model.add_task(task)
        self.view.update_task(task_id, task.name)
