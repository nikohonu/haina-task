import typing

import typer

from haina_task.view import View


class TyperView(View):
    def __init__(self) -> None:
        super().__init__()
        self.app = typer.Typer()

    def setup(self, controller: typing.Any) -> None:
        self.controller = controller

    def start(self) -> None:
        if not self.controller:
            raise NameError("Controller isn't setup")

        @self.app.command()
        def add(name: str) -> None:
            self.controller.add_task(name)

        @self.app.command()
        def edit(item: str) -> None:
            print(f"Deleting item: {item}")

        @self.app.command()
        def done(item: str) -> None:
            print(f"Selling item: {item}")

        @self.app.command()
        def agenda(item: str) -> None:
            print(f"Selling item: {item}")

        @self.app.command()
        def today(item: str) -> None:
            print(f"Selling item: {item}")

        self.app()

    def update_task(self, task_id: int, name: str) -> None:
        print(f'task "{name} with id {task_id} was added')
