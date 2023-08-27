import typing
from datetime import datetime, time
from typing import List, Optional

import typer
from typing_extensions import Annotated

from haina_task.models.task import Task
from haina_task.views.view import View


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
        def add(
            name: str,
            chain: Annotated[Optional[list[str]], typer.Option()] = None,
            description: Annotated[Optional[str], typer.Option()] = None,
            schedule: Annotated[Optional[datetime], typer.Option()] = None,
            deadline: Annotated[Optional[datetime], typer.Option()] = None,
            recurence: Annotated[Optional[str], typer.Option()] = None,
            project: Annotated[Optional[str], typer.Option()] = None,
        ) -> None:
            if deadline and schedule:
                if deadline <= schedule:
                    print("Deadline must can't be smaller than schedule.")
                    raise typer.Exit()
            if recurence and not schedule:
                schedule = datetime.now().replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
            self.controller.add_task(
                Task(name, chain, description, schedule, deadline, recurence, project)
            )

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
