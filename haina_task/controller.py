from haina_task.model import Model
from haina_task.typer_view import TyperView


class Controller:
    def __init__(self, model: Model, view: TyperView) -> None:
        self.model = model
        self.view = view

    def start(self) -> None:
        self.view.setup(self)
        self.view.start()

    def add_task(self, name: str) -> None:
        task_id = self.model.add_task(name)
        self.view.update_task(task_id, name)

